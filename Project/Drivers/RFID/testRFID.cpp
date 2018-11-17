#include <stdio.h>
#include <iostream>
#include <wiringPi.h>
#include "Rfid.hpp"

int main (void)
{
	Rfid test;
	uint8_t tag[6] = {0x18, 0x09, 0x00, 0x00, 0x91, 0x80};
	uint8_t compare[6] = {0, 0, 0, 0, 0, 0};
	uint8_t match = 0;
	uint8_t toggle = 1;

	test.Initialize();
	test.SetTag(tag);

	wiringPiSetup();
	pinMode(4, OUTPUT);
	pinMode(5, OUTPUT);	
	digitalWrite(4,toggle);
	digitalWrite(5, LOW);

	while (1)
	{
		while (!match){
			compare = test.GetTag();
			if (compare[5] != 0)
				match = 1;
		}
		if (test.CompareTag(tag, compare))
		{
			toggle ^= toggle;
			digitalWrite(4, toggle);
			digitalWrite(5, HIGH);
		}
		
		match = 0;
	}
	
}
