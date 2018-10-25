#pragma once

class Servo
{
public:
	enum RotateMode : uint8_t
	{
		kFull = 0;  // These numbers will change based on PWM
		kHalf = 1;  // values and ranges needed for servos.
		k8th  = 2;
	};

        Servo();
	void Init();
	void OpenDoor(); //Set as false by default
        void CloseDoor();
	void RotateFeed(ServoDriver::RotateAmount amount);
};
