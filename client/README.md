#### Installation
Install https://github.com/eclipse/paho.mqtt.c

```
apt-get install build-essential gcc make cmake fakeroot fakeroot devscripts \
                dh-make lsb-release libssl-dev doxygen graphviz
```

cd into the mqtt directory

```
make
sudo make install
```

Install https://github.com/eclipse/paho.mqtt.cpp
```
git clone https://github.com/eclipse/paho.mqtt.cpp
cd paho.mqtt.cpp
mkdir build
cd build
cmake -DPAHO_BUILD_DOCUMENTATION=TRUE -DPAHO_BUILD_SAMPLES=TRUE -DPAHO_MQTT_C_PATH=../../paho.mqtt.c ..
make
sudo make install
```

Make sure shared libraries can be found
```
sudo ldconfig
```




#### Issues encountered with paho.mqtt.cpp:

-  error while loading shared libraries: libpaho-mqttpp3.so.1

Make sure libpaho-mqttpp3.so.1 exists in /usr/local/lib/ and make sure sudo make install was run in paho.mqtt.cpp. Then run
```
sudo ldconfig
```

