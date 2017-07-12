#define SAMPLING 300
#define VOFFSET 512
#define ADC_PIN A1
//Port A1 = Voltage inner
#define AMPLITUDE 400
#define REAL_VAC 230
int ADC_MAX, ADC_MIN;
int ADC_VPP;


int analogInPin = A0; // Analog input pin that the carrier board OUT is connected to
int sensorValue = 0; // value read from the carrier board
int outputValue = 0; // output in milliamps


void setup()
{
  Serial.begin(9600);
}
//
//void loop()
//{
// read_VAC();
// float V = map(ADC_VPP,0,AMPLITUDE,0,REAL_VAC*100.0); // Calculate in deep wait for measurement part
//  V /= 100;
// String data;
// data = "Voltage = "+String(V,1)+(" VAC");
// Serial.println(data);
// delay(1000); // 1 Second define
//}
//void loop()
//{
//  float average = 0;
//  for(int i = 0; i < 1000; i++)
//  {
//    average = average + (.0264 * analogRead(ADC_PIN) -13.51) / 1000;
//    delay(1);
//  }
//  Serial.println(average);
//}
//void loop() {
//  // read the analog in value:
//  sensorValue = analogRead(ADC_PIN);
//
//  // convert to milli amps
//  outputValue = (((long)sensorValue * 5000 / 1024) - 500 ) * 1000 / 133;
//
//  /* sensor outputs about 100 at rest. Analog read produces a value of 0-1023, equating to 0v to 5v. "((long)sensorValue * 5000 / 1024)" is the voltage on the sensor's output in millivolts. There's a 500mv offset to subtract. The unit produces 133mv per amp of current.*/
//
//  // print the results to the serial monitor:
//  Serial.print("sensor = " );
//  Serial.print(sensorValue);
//  Serial.print("\t Current (ma) = ");
//  Serial.println(outputValue/100);
//
//  // wait 10 milliseconds before the next loop
//  // for the analog-to-digital converter to settle // after the last reading:
//  delay(500);
//}
void read_VAC()
{
  int cnt;
  ADC_MAX = 0;
  ADC_MIN = 1024;
  for (cnt = 0; cnt < SAMPLING; cnt++)
  {
    int adc = analogRead(ADC_PIN);
    ADC_MAX = adc > ADC_MAX ? adc : ADC_MAX;
    ADC_MIN = adc < ADC_MIN ? adc : ADC_MIN;

  }
  ADC_VPP = ADC_MAX - ADC_MIN;
}
