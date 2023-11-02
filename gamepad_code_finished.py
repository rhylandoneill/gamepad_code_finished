# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""
import binascii #imports libraries that are needed to run this code
import board
import busio
import digitalio
import time
import pwmio

from dabble import Dabble #imports the library called Dabble that Mr. Ayers wrote

dabble = Dabble(board.GP0, board.GP1, debug=True) #initiates Dabble and attaches it to pins GP0 and GP1

from adafruit_motor import motor #imports a small section of the adafruit_motor library

left_motor_forward = board.GP12 #Initializes the variable left_motor_forward and attaches it to GP12
left_motor_backward = board.GP13 #Initializes the variable left_motor_backward and attaches it to GP13
right_motor_forward = board.GP16 #Initializes the variable right_motor_forward and attaches it to GP16
right_motor_backward = board.GP17 #Initializes the variable right_motor_backward and attaches it to GP17

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Rc = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Rd = pwmio.PWMOut(right_motor_backward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Initializes Left_Motor and cnfiguration line and it is required
Left_Motor_speed = 0 #Initializes the variable Left_Motor_speed to 0
Right_Motor = motor.DCMotor(pwm_Rc, pwm_Rd) #Initializes Right_Motor and configuration line and it is required
Right_Motor_speed = 0 #Initializes the variable Right_Motor_speed to 0

def forward():
    Left_Motor_speed = 1 #Left Motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Right Motor forward
    Right_Motor.throttle = Right_Motor_speed

def backward():
    Left_Motor_speed = -1 #Left Motor backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right Motor backward
    Right_Motor.throttle = Right_Motor_speed

def left():
    Left_Motor_speed = -1 #Left Motor backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Right Motor forward
    Right_Motor.throttle = Right_Motor_speed

def right():
    Left_Motor_speed = 1 #Left Motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right Motor backward
    Right_Motor.throttle = Right_Motor_speed

def stop():
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0
    Right_Motor.throttle = Right_Motor_speed

while True:
    message = dabble.read_message() #command to take input from the bluetooth module
    if (message != None):
        print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            forward()
            print("Move both motors forward")
        elif (message.down_arrow_pressed):
            backward()
            print("Move both motors backward")
        elif (message.right_arrow_pressed):
            right()
            print("Move left motor forward and right motor backward")
        elif (message.left_arrow_pressed):
            left()
            print("Move left motor backward and right motor forward")
        elif (message.no_direction_pressed):
            stop()
            print("Stop both motors")
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
