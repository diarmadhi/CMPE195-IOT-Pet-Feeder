#!/bin/bash
# Setup a base directory:
SJBASE="/home/CMPE-195-IOT-Pet-Feeder"

# SJSUOne Board Settings:
#SJDEV="/dev/ttyUSB0" # Set this to your board ID
#SJBAUD=38400

# Project Target Settings:
# Sets the binary name, defaults to "firmware" (Optional)
#SJPROJ=firmware

# Sets which DBC to generate, defaults to "DBG"
#ENTITY=DBG

# Sets CLANG tools path
SJCLANG=$SJBASE/tools/clang+llvm-6.0.1-x86_64-linux-gnu-ubuntu-16.04/bin

# Compiler and library settings:
# Selects compiler version to use
#PATH=$(printf %q "$PATH:$SJBASE/tools/gcc-arm-none-eabi-7-2017-q4-major/bin")
PATH=$(printf %q "$PATH:$SJCLANG")
#SJLIBDIR="$SJBASE/firmware/library"

# Export everything to the environment
export SJBASE
#export SJDEV
#export SJBAUD
#export SJPROJ
export SJCLANG
#export ENTITY
export PATH
#export SJLIBDIR
