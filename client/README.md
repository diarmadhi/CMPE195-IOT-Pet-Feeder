Issues encountered with paho.mqtt.cpp:

-  error while loading shared libraries: libpaho-mqttpp3.so.1

Make sure libpaho-mqttpp3.so.1 exists in /usr/local/lib/ and make sure sudo make install was run in paho.mqtt.cpp. Then run
```
sudo ldconfig
```

