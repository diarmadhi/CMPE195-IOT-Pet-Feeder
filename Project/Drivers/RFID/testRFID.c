	
//compile with g++ -o test test.c -l wiringPi
// pinout for wiring pi on pinout.xyz/pinout/wiringpi#

#include <stdio.h>
#include <iostream>
#include <wiringPi.h>
#include <unistd.h>
#include <string.h>
#include "Rfid.hpp"

using namespace std;

int main(void){
	wiringPiSetup();
	int choice;
	pinMode(4, OUTPUT);
	pinMode(5, OUTPUT);
	digitalWrite(4, LOW);
	digitalWrite(5, LOW);

	Rfid test;
//	uint8_t tag[6] = {0x18, 0x09, 0x00, 0x00, 0x91, 0x80};
//	uint8_t *compare;
	string tag = "55003AAA8540";
	string compare;

printf("test tag: %s\n", tag.c_str());  //works for printing strings
//printf("size of tag: %d\n", tag.size());
	test.Initialize();
	test.SetTag(tag);

	printf("Starting Program\n");

	while(true){
		test.GetTag(compare);
		if (test.CompareTag(tag, compare))
		{
printf("compare tag: %s\n", compare.c_str());
			printf("Tags Match! Blue LED is on\n");
			digitalWrite(4, HIGH);
			digitalWrite(5, LOW);
			compare = "0"; 	
		} 
		else if (!test.CompareTag(tag, compare) && compare != "0")
		{
printf("compare tag: %s\n", compare.c_str());
//printf("size of compare: %d\n", compare.size());
			printf("Tags don's match. Red LED is on\n");
			digitalWrite(4, LOW);
			digitalWrite(5, HIGH);
			compare = "0";
		} 

//		switch(choice){
  //         		case 1:
//				digitalWrite(4, HIGH);
  //            	  		break;
    //      	  	case 2:
//				digitalWrite(4, LOW);
  //        	      		break;
    //    	    	case 3:
//				output = digitalRead(5);
//				printf("output: %d\n", output);
//				if(output) printf("signal on\n");
//				else printf("signal off\n");
  //     	         		break;
    //    	    	default:
      //   	       		break;

		/*output = digitalRead(5);
		printf("output: %d\n", output);
		sleep(1);*/
	//	}
	}
}
