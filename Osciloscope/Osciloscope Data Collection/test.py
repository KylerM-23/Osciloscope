import random as R
import math as M
from graphics import *
import Tkinter as TK
import time as T
from time import sleep
from ina219 import INA219

def main():
	dt = 1
	t = 5
	ina  = INA219(shunt_ohms = 0.1, max_expected_amps = 1, address = 0x40)
	ina.configure(voltage_range = ina.RANGE_16V, gain=  ina.GAIN_AUTO, bus_adc = ina.ADC_128SAMP, shunt_adc = ina.ADC_128SAMP)
	time = []
	volt = []
	i = 0
	while(i<=t):
		time.append(i)
		print(ina.voltage())
		print(ina.current())
		print(ina.power())
		volt.append(ina.voltage())
		i = i + dt
		sleep(dt)
        
        
main()
