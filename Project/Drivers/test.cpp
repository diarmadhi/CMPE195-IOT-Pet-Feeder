#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <unistd.h>

using namespace std;

int main()
{
cout << "hi" << endl;
system("echo 1=60% > /dev/servoblaster");
sleep(1);
cout << "hello" << endl;
system("echo 1=40% > /dev/servoblaster");
sleep(1);
system("echo 1=50% > /dev/servoblaster");
};
