#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
turn_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
touch_sensor = TouchSensor(Port.S1)

def calibrate_arm():
    """Resets the robot arm position"""
    color = color_sensor
    claw = claw_motor
    limit_sensor = touch_sensor
    base_motor = turn_motor
    elbow_motor = arm_motor
    i = 1
    while (color.reflection()) < 36:
        #print(color.reflection())
        #print(elbow_motor.angle()) 
        # Raise the arm to lift the wheel stack.
        elbow_motor.run_angle(30, 20)
        wait(200)
    while color.reflection() > 0:
        #print(color.reflection())
        #print(elbow_motor.angle()) 
        # Raise the arm to lift the wheel stack.
        elbow_motor.run_angle(30, -20)
        wait(200)
    while claw.angle() < 75:
        # Raise the arm to lift the wheel stack.
        claw.run_angle(30, 25)
        print(claw.angle())
        if claw.angle() < 25 * i:
            claw.run_angle(30, -75)
            break
        i += 1


        wait(200)
    while not limit_sensor.pressed():
        print(limit_sensor.pressed())
        # Rotate to the pick-up position.
        base_motor.run_angle(20, 25)
        wait(200)
    print("robot calibrated")


def pickup(position):
    # Rotate to the pick-up position.
    base_motor = turn_motor
    base_motor.run_target(60, position)

    # Lower the arm.
    elbow_motor = arm_motor
    elbow_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=50)

    # Close the gripper to grab the wheel stack.
    gripper_motor = claw_motor
    gripper_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=100)

    # Raise the arm to lift the wheel stack.
    elbow_motor.run_target(-300, -200) 
    #while True:
        #gripper_motor.run_until_stalled(600, then=Stop.HOLD, duty_limit=50)
        #wait(10)

def drop():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)
def color_recognition():
    return color_sensor.color()



# Write your program here.
calibrate_arm()
pickup(-100)
drop()

