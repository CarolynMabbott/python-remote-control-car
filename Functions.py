#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import pygame
import os
pygame.init()
GPIO.setmode(GPIO.BCM)
Start_button = 3

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 25
coil_B_1_pin = 24
coil_B_2_pin = 23
coil_A_3_pin = 17
coil_A_4_pin = 18
coil_B_3_pin = 27 
coil_B_4_pin = 22

GPIO.setup(enable_pin,GPIO.OUT)
GPIO.setup(coil_A_1_pin,GPIO.OUT)
GPIO.setup(coil_A_2_pin,GPIO.OUT)
GPIO.setup(coil_B_1_pin,GPIO.OUT)
GPIO.setup(coil_B_2_pin,GPIO.OUT)
GPIO.setup(coil_A_3_pin,GPIO.OUT)
GPIO.setup(coil_A_4_pin,GPIO.OUT)
GPIO.setup(coil_B_3_pin,GPIO.OUT)
GPIO.setup(coil_B_4_pin,GPIO.OUT)

#Left hand motor
def setStepM1(w1, w2, w3, w4):
	GPIO.output(coil_A_1_pin, w1)
	GPIO.output(coil_A_2_pin, w2)
	GPIO.output(coil_B_1_pin, w3)
	GPIO.output(coil_B_2_pin, w4)
#Right hand motor
def setStepM2(w1, w2, w3, w4):
	GPIO.output(coil_A_3_pin, w1)
	GPIO.output(coil_A_4_pin, w2)
	GPIO.output(coil_B_3_pin, w3)
	GPIO.output(coil_B_4_pin, w4)


GPIO.setup(2, GPIO.IN)

def forward(delay):
	setStepM1(1, 1, 0, 0)
	setStepM2(1, 1, 0, 0)
	time.sleep(delay)
	setStepM1(0, 1, 1, 0)
	setStepM2(0, 1, 1, 0)
	time.sleep(delay)
	setStepM1(0, 0, 1, 1)
	setStepM2(0, 0, 1, 1)
	time.sleep(delay)
	setStepM1(1, 0, 0, 1)
	setStepM2(1, 0, 0, 1)
	time.sleep(delay)

def backwards(delay):
	setStepM1(0, 0, 1, 1)
	setStepM2(0, 0, 1, 1)
	time.sleep(delay)
	setStepM1(0, 1, 1, 0)
	setStepM2(0, 1, 1, 0)
	time.sleep(delay)
	setStepM1(1, 1, 0, 0)
	setStepM2(1, 1, 0, 0)
	time.sleep(delay)
	setStepM1(1, 0, 0, 1)
	setStepM2(1, 0, 0, 1)
	time.sleep(delay)

def right(delay):
	setStepM1(1, 1, 0, 0)
	setStepM2(0, 0, 1, 1)
	time.sleep(delay)
	setStepM1(0, 1, 1, 0)
	setStepM2(0, 1, 1, 0)
	time.sleep(delay)
	setStepM1(0, 0, 1, 1)
	setStepM2(1, 1, 0, 0)
	time.sleep(delay)
	setStepM1(1, 0, 0, 1)
	setStepM2(1, 0, 0, 1 )
	time.sleep(delay)

def left(delay):
	setStepM1(0, 0, 1, 1)
	setStepM2(1, 1, 0, 0)
	time.sleep(delay)
	setStepM1(0, 1, 1, 0)
	setStepM2(0, 1, 1, 0)
	time.sleep(delay)
	setStepM1(1, 1, 0, 0)
	setStepM2(0, 0, 1, 1)
	time.sleep(delay)
	setStepM1(1, 0, 0, 1)
	setStepM2(1, 0, 0, 1)
	time.sleep(delay)

def auto(delay):
	while True:
		forward(delay)
		if joystick.get_button(Start_button):
			os.system('sudo shutdown -h now')
			break
		if(GPIO.input(2) == 1):
			#print 'switch not pressed'
			time.sleep(delay)
		if(GPIO.input(2) == 0):
			#print 'switch pressed'
			time.sleep(0.5)
			#auto(delay)	
			#go backwards
			for i in range(0, 100):
				backwards(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
				break
			#turn right
			for i in range(0, 400):
				right(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
				break				
			#go forwards
			for i in range(0, 400):
				forward(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break				
			#go left
			for i in range(0, 400):
				left(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break				
			#go forwards
			for i in range(0, 800):
				forward(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break				
			#go left
			for i in range(0, 400):
				left(delay)				
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break	
			#go right
			for i in range(0, 400):
				right(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break				
			#go forwards
			for i in range(0, 400):
				forward(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break				
			#go right
			for i in range(0, 400):
				right(delay)
				if joystick.get_button(Start_button):
					os.system('sudo shutdown -h now')
					break
	
GPIO.cleanup()
