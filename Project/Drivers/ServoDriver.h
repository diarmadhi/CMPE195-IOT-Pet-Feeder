
#ifndef SERVO_DRIVER_H
#define SERVO_DRIVER_H

/*
DRAFT of Servo Driver
*/

class ServoDriver
{
public:
	enum RotationAmount : uint8_t
	{
		kFull = 100; // These numbers will change based on PWM
		kHalf = 50;  // values and ranges needed for servos.
		k8th  = 12.5;
	};
    ServoDriver();
	void Init();
	void OpenDoor(bool OpenBowl = false); //Set as false by default
	void RotateFeed(ServoDriver::RotationAmount amount);
};

#endif SERVO_DRIVER_H
