#define SAMPLING 300 // ตัวอย่างการสุ่มค่าต่อการคำนวณ
#define VOFFSET 512 //ออฟเซ็ตของ โวลต์ 2.5V จาก 10 Bit
#define AMPLITUDE 401 //Amplitude คลื่น ของ อนาล็อก
#define REAL_VAC 230.5 // โวลต์กระแสจริง
int ADC_MAX, ADC_MIN; //ADC min max หาเฉลี่ยของอนาล็อกคลื่น
int ADC_VPP; // ADC VPP = Voltage สุดท้าย

#define CALIBRATE_AMPS -0.13

int mVperAmp = 66; // use 100 for 20A Module and 66 for 30A Module
 
double Voltage = 0;
double VRMS = 0;
double AmpsRMS = 0;

const int sensorIn = A0;
const int sensorVoltage = A1;

void setup() {
  Serial.begin(9600);
}

void loop() {

  double voltage = read_VAC();
  //Serial.print(voltage);
  //Serial.print(" , ");
  double value = analogRead(sensorIn);
  double amps = getVPP()+CALIBRATE_AMPS;
  //Serial.println((((value-510.0)*5.0)/1023.0)/0.0645);
 //Serial.println();
 double finalpower = voltage*amps;
 Serial.print("Power = " );
 Serial.println(finalpower);
 
  delay(250);
}


double read_VAC()
{
  int cnt;
  ADC_MAX = 0;
  ADC_MIN = 1024;
  for (cnt = 0; cnt < SAMPLING; cnt++)
  {
    int adc = analogRead(sensorVoltage);
    ADC_MAX = adc > ADC_MAX ? adc : ADC_MAX;
    ADC_MIN = adc < ADC_MIN ? adc : ADC_MIN;

  }
  ADC_VPP = ADC_MAX - ADC_MIN;
  //float V = (ADC_VPP*5.0)/1024.0;
  float V = map(ADC_VPP, 0, AMPLITUDE, 0, REAL_VAC * 100.0) / 100.0; // Calculate in deep wait for measurement part
  return V;
}
double getVPP()
{
  double result;
  int readValue;             //value read from the sensor
  int maxValue = 0;          // store max value here
  int minValue = 1024;          // store min value here
  
   uint32_t start_time = millis();
   while((millis()-start_time) < 1000) //sample for 1 Sec
   {
       readValue = analogRead(sensorIn);
       maxValue = readValue>maxValue ? readValue:maxValue;
       minValue = readValue<minValue ? readValue:minValue;
   }
   
   // Subtract min from max
   result = ((maxValue - minValue) * 5.0)/1024.0;
   VRMS = (result/2.0) *0.7071067811865475;  //root 2 is 0.707
   AmpsRMS = (VRMS * 1000)/mVperAmp;
   return result=AmpsRMS;
 }
