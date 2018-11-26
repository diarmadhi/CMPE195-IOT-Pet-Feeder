#pragma once

#include <wiringSerial.h>
#include <string>
#include <errno.h>

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
//		else {
//			for (uint8_t i = 0; i < 6; i++)
//			{
//				programmed_tag[i] = 0;
//				read_tag[i] = 0;
//			}
//		}
	}

//	void SetTag(uint8_t *tag)
	void SetTag(string &tag)
	{
//		for (uint8_t i = 0; i < 6; i++)
//		{
//			programmed_tag[i] = tag[i];
		programmed_tag = tag;
//		}
	}
	
//	uint8_t * GetTag()
	void GetTag(string &tag)
	{
		int dataAvailable = serialDataAvail(handle);	//works
		char read_tag[dataAvailable];

		if (dataAvailable == -1)
		{
			printf("Data error: %s\n", strerror(errno));
		}
		else if (dataAvailable > 8) {  //reader outputs 16 bytes for tag id
			for (int i = 0; i < dataAvailable; i++)	//pull data from rx reg
			{
//	printf("%c",(char) serialGetchar(handle));
//				read_tag[i] = serialGetchar(handle);	//works
//				tag += read_tag[i];	//works
				tag += (char) serialGetchar(handle);  //works <-better option
			}
			tag = tag.substr(2,12);
//	printf("%s\n", tag.c_str());
		} else tag = "0";

//		return read_tag;
	}

	bool CompareTag(string &tag1, string &tag2)
	{
		uint8_t match = 0;
//		for (uint8_t i = 0; i < 6; i++)
//		{
//			if (programmed_tag[i] != read_tag[i])
//			{
//				match = 0;
//				return match;
//			}
//			match = 1;
//		}
		if (tag1 != tag2)
			match = 0;
		else match = 1;
		return match;
	}

	Rfid()
	{
//		for (uint8_t i = 0; i < 6; i++)
//		{
//			read_tag[i] = 0;
//		}
	}

	~Rfid()
	{
	}

private: 
//	uint8_t programmed_tag[6];
//	uint8_t read_tag[16];
	string programmed_tag;
//	string read_tag;
	int handle = 0;
};


