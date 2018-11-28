#pragma once

#include <wiringSerial.h>
#include <string>
#include <errno.h>
#include <sstream>
#include <iomanip>

using namespace std;

class Rfid
{
public: 
	void Initialize()
	{
		handle = serialOpen("/dev/ttyAMA0", 9600);
		if (handle < 0)
		{
			printf("Initialize error: %s\n", strerror(errno));
		}
	}

	void SetTag(string &tag)
	{
		string temp = "0002520309";
		uint32_t convert = stoul(temp, nullptr); //convert string to uint - "1234" to 1234
		stringstream ss; //used to create a hex based string from convert

		ss << uppercase << hex << setw(8) << setfill('0') << convert; //creates an 8 digit hex stream of convert with leading zeros
		programmed_tag = ss.str(); //converts stream to string
	}
	

	void GetTag(string &tag)
	{
		int dataAvailable = serialDataAvail(handle);	//works

		if (dataAvailable == -1)
		{
			printf("Data error: %s\n", strerror(errno));
		}
		else if (dataAvailable > 8) {  //reader outputs 16 bytes for tag id
			for (int i = 0; i < dataAvailable; i++)	//pull data from rx reg
			{
				tag += (char) serialGetchar(handle);  //works <-better option
			}
			tag = tag.substr(4,8);

		} else tag = "0";

	}

	bool CompareTag(string &tag)
	{
		uint8_t match = 0;

		if (tag != programmed_tag)
			match = 0;
		else match = 1;
		return match;
	}

	Rfid()
	{
	}

	~Rfid()
	{
	}

private: 
	string programmed_tag;
	int handle = 0;
};


