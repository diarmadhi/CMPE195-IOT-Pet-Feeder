PAHO_CPP_DIR ?= /home/pi/paho.mqtt.cpp
PAHO_C_DIR ?= /home/pi/paho.mqtt.c

ifdef DEVELOP
  PAHO_C_LIB_DIR ?= $(PAHO_C_DIR)/build/output
  PAHO_C_INC_DIR ?= $(PAHO_C_DIR)/src
else
  PAHO_C_LIB_DIR ?= /usr/local/lib
  PAHO_C_INC_DIR ?= /usr/local/include
endif

TARGET = main

all: $(TARGET)

CXXFLAGS += -Wall -std=c++11 -g -O0
CPPFLAGS += -DOPENSSL -I$(PAHO_C_INC_DIR) -I$(PAHO_CPP_DIR)/src

CC = gcc
CXX = g++

LDLIBS += -L$(PAHO_CPP_DIR)/lib -L$(PAHO_C_LIB_DIR) -lpaho-mqttpp3 -lpaho-mqtt3a
LDLIBS_SSL += -L$(PAHO_CPP_DIR)/lib -L$(PAHO_C_LIB_DIR) -lpaho-mqttpp3 -lpaho-mqtt3as

main: main.cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -o $@ $< $(LDLIBS)
