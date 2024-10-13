#include<stdio.h>
#include<wiringPi.h>
#define Pin 7

int main()
{
	if (wiringPiSetup() < 0)
		return 1;
	pinMode(Pin,OUTPUT);
	for(int i = 0;i < 10; i++)
	{
		digitalWrite(Pin,1);
		delay(200);
		digitalWrite(Pin,0);
		delay(200);
	}
	return 0;
}
