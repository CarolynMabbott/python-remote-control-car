#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import pygame
GPIO.setmode(GPIO.BCM)
import functions
import os

pygame.init()

#Key mappings for each button used
x_button = 14
R1_button = 11
L1_button = 10
Triangle_button = 12
Square_button = 15
Left_button = 7
Right_button = 5
Start_button = 3

#Set the GPIO pins
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 25
coil_B_1_pin = 24
coil_B_2_pin = 23
coil_A_3_pin = 17
coil_A_4_pin = 18
coil_B_3_pin = 27 
coil_B_4_pin = 22

#Set up the GPIO pins to output
GPIO.setup(enable_pin,GPIO.OUT)
GPIO.setup(coil_A_1_pin,GPIO.OUT)
GPIO.setup(coil_A_2_pin,GPIO.OUT)
GPIO.setup(coil_B_1_pin,GPIO.OUT)
GPIO.setup(coil_B_2_pin,GPIO.OUT)
GPIO.setup(coil_A_3_pin,GPIO.OUT)
GPIO.setup(coil_A_4_pin,GPIO.OUT)
GPIO.setup(coil_B_3_pin,GPIO.OUT)
GPIO.setup(coil_B_4_pin,GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
#Set up Switch pins to input
GPIO.setup(2, GPIO.IN)
#Set the LED to off
GPIO.output(3, False)

try:
	#Get joystick connected
	joystick = pygame.joystick.Joystick(0)
	joystick.init() 
	#Delay that is needed to send to the move functions
	delay = (2.0 / 1000.0)
	#LEDstate is set to 0 when it is off
	LEDstate = 0

	while True:

		pygame.event.clear()
		pygame.event.get()
		if joystick.get_button(R1_button):
			#Can slow down speed
			#Once square isnt pressed speed goes back to normal
			if joystick.get_button(Square_button):
				delay = (10.0/ 1000.0)
			else:
				delay = (2.0/ 1000.0)
			functions.forward(delay)		
		if joystick.get_button(L1_button):
			functions.backwards(delay)
		if joystick.get_button(Right_button):
			functions.right(delay)	
		if joystick.get_button(Left_button):
			functions.left(delay)
		if joystick.get_button(Triangle_button):
			functions.auto(delay)							
		if joystick.get_button(x_button):
			if LEDstate == 0:
				GPIO.output(3, True)
				LEDstate = 1
			elif LEDstate == 1:	
				GPIO.output(3, False)
				LEDstate = 0	
		if joystick.get_button(Start_button):
			os.system('sudo shutdown -h now')
			break

except KeyboardInterrupt:
	#Turns off all lights when program stops and turns the LED on
	GPIO.cleanup()
	GPIO.output(3, True)
