#define SAMPLING 300
#define VOFFSET 512
#define ADC_PIN A0 
#define AMPLITUDE 411.00 
#define REAL_VAC 233.5 
int ADC_MAX,ADC_MIN;
int ADC_VPP;
void setup()
{
 Serial.begin(9600);
}
void loop()
{
 read_VAC(); 
 float V = map(ADC_VPP,0,AMPLITUDE,0,REAL_VAC*100)/100.00; // Calculate in deep wait for measurement part

 String data;
 data = "Voltage = "+String(V,1)+(" VAC");
 Serial.println(data);
 delay(1000); // 1 Second define
}
void read_VAC()
{
 int cnt;
 ADC_MAX = 0;
 ADC_MIN = 1024;
 for(cnt=0;cnt<SAMPLING;cnt++)
 {
    int adc = analogRead(ADC_PIN);
    ADC_MAX = adc>ADC_MAX ? adc:ADC_MAX;
    ADC_MIN = adc < ADC_MIN ? adc:ADC_MIN;
 }
}
