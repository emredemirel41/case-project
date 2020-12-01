"""
import machine

machine.freq()          # get the current frequency of the CPU
machine.freq(160000000) # set the CPU frequency to 160 MHz

try:
  import usocket as socket
except:
  import socket
  
import ussl as ssl

from machine import Pin
import network

import esp
esp.osdebug(None)

print("Run Boot")

import Connect_Wifi 
Connect_Wifi.do_connect()  # Connection Auto 

import gc
gc.collect()

from machine import Pin
led = Pin(2, Pin.OUT)
    """