	
//compile with g++ -o test test.c -l wiringPi
// pinout for wiring pi on pinout.xyz/pinout/wiringpi#

#include <stdio.h>
#include <iostream>
#include <wiringPi.h>
#include <unistd.h>

using namespace std;

int main(void){
	wiringPiSetup();
	int choice;
	pinMode(4, OUTPUT);
	pinMode(5, INPUT);
	int output = 5;
	printf("Starting Program\n");

	while(true){
		printf("\n1. GPIO ON\n2. GPIO OFF\n3. READ GPIO\n");
        	scanf("%d", &choice);
        	switch(choice){
           		case 1:
				digitalWrite(4, HIGH);
              	  		break;
          	  	case 2:
				digitalWrite(4, LOW);
          	      		break;
        	    	case 3:
				output = digitalRead(5);
				printf("output: %d\n", output);
				if(output) printf("signal on\n");
				else printf("signal off\n");
       	         		break;
        	    	default:
         	       		break;

		/*output = digitalRead(5);
		printf("output: %d\n", output);
		sleep(1);*/
		}
	}
}
