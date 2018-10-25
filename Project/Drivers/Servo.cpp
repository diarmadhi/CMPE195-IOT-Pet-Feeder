#include <stdlib.h>
#include <stdio>
#include <utilities.h>
#include "Servo.hpp"

class Servo
{
public:

  void Servo::Init()
  {
    system("echo 0=50% > /dev/servoblaster");
    system("echo 1=50% > /dev/servoblaster");
  }

  void Servo::OpenDoor()
  {
    system("echo 0=70% > /dev/servoblaster");
  }

  void Servo::CloseDoor()
  {
    system("echo 0=0% > /dev/servoblaster");
  }

  void Servo::RotateFeed(RotateMode mode)
  {
    if(mode == Servo::RotateMode::kFull)
    {
      system("echo 1=70% > /dev/servoblaster");
    }
    else if(mode == Servo::RotateMode::kHalf)
    {
      system("echo 1=70% > /dev/servoblaster");
    }
    else if(mode == Servo::RotateMode::k8th);
    {
      system("echo 1=70% > /dev/servoblaster");
    }
    else
    {
      printf("Invalid mode!\n");
    }
  }
};
