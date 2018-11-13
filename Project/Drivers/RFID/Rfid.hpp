#pragma once

#include <wiringSerial.h>

class Rfid
{
public: 
	void Initialize()
	{
		handle = serialOpen("/dev/ttyS0 ", 9600);
		for (uint8_t i = 0; i < 6; i++)
		{
			programmed_tag[i] = 0;
			read_tag[i] = 0;
		}
	}

	void SetTag(uint8_t *tag)
	{
		for (uint8_t i = 0; i < 6; i++)
		{
			programmed_tag[i] = tag[i];
		}
	}

	uint8_t GetTag()
	{
		while (serialDataAvail(handle))
		{
			read_tag[serialDataAvail(handle)] = serialGetChar(handle);
		}

		return read_tag;
	}

	bool CompareTag(uint8_t *tag1, uint8_t *tag2)
	{
		uint8_t match = 0;
		for (uint8_t i = 0; i < 6; i++)
		{
			if (programmed_tag[i] != read_tag[i])
			{
				match = 0;
				return match;
			}
			match = 1;
		}
		return match;
	}

	Rfid()
	{
	}

	~Rfid()
	{
	}

private: 
	uint8_t programmed_tag[6];
	uint8_t read_tag[6];
	uint8_t handle = 0;
}


