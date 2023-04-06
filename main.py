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
color_sensor = Motor(Port.S2)


# Write your program here.
ev3.speaker.beep()
arm_motor.run_until_stalled(-100, then=Stop.COAST, duty_limit=100)
claw_motor.run_time(50, 3000, then=Stop.HOLD, wait=True)
arm_motor.run_until_stalled(70, then=Stop.COAST, duty_limit=50)
claw_motor.run_time(-50, 2000, then=Stop.HOLD, wait=True)

def drop():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)