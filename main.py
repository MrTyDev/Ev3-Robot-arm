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



# Write your program here.
ev3.speaker.beep()


def pickup(position):
    # Rotate to the pick-up position.
    base_motor = turn_motor
    base_motor.run_target(60, position)

    # Lower the arm.
    elbow_motor = arm_motor
    elbow_motor.run_target(60, -40)

    # Close the gripper to grab the wheel stack.
    gripper_motor = claw_motor
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)

    # Raise the arm to lift the wheel stack.
    elbow_motor.run_target(60, 0) 

def drop():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)