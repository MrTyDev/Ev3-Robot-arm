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
    while (color.reflection()) < 36:
       
        #print(elbow_motor.angle()) 
        # Raise the arm to lift the wheel stack.
        elbow_motor.run_angle(50, 25)
        
    while color.reflection() > 0:

        #print(elbow_motor.angle()) 
        # Raise the arm to lift the wheel stack.
        elbow_motor.run_angle(50, -25)
    
        
 
    drop()
            
    while not limit_sensor.pressed():
        # Rotate to the pick-up position.
        base_motor.run_angle(50, 25)
        print(base_motor.angle())
        

    print("robot calibrated")
    return base_motor.reset_angle(0)

def pickup(position,elbow_taget):
    # Rotate to the pick-up position.
    base_motor = turn_motor
    base_motor.run_angle(60, position)

    # Lower the arm.
    elbow_motor = arm_motor
    elbow_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=50)

    # Close the gripper to grab the wheel stack.
    gripper_motor = claw_motor
    gripper_motor.reset_angle(0)
    gripper_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=100)
    print(gripper_motor.angle())
    if gripper_motor.angle()>85:
        gripper_motor.run_angle(100,-100)

    # Raise the arm to lift the wheel stack.
    elbow_motor.reset_angle(0)
    elbow_motor.run_target(-100, elbow_taget)
    #print(base_motor.angle())
    wait(500)
    if color_recognition() == Color.RED or color_recognition() == Color.BLUE:
        print(color_recognition())
        print("YAAAAAAY")
        wait(5000)
    else:
        print("Nothing here to pick up")
    wait(500)

def drop():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)

def color_recognition():
    return color_sensor.color()

def drop_at_pos(position):
    turn_motor.run_target(-100, position)
    arm_motor.run_target(-100, 150)
    drop()
    arm_motor.run_target(-100, -150)

    current_color =  color_recognition()

    if current_color == Color.BLUE:
        drop_at_pos(0)
    elif current_color == Color.RED:
        drop_at_pos(-700)
    elif current_color == Color.YELLOW:
        drop_at_pos(-700)
    elif current_color == Color.GREEN:
        drop_at_pos(-350)
    else:
        drop_at_pos(-350)




# Write your program here.
calibrate_arm()
pickup(-350,-425)

current_color =  color_recognition()

if current_color == Color.BLUE:
    drop_at_pos(0)
elif current_color == Color.RED:
    drop_at_pos(-700)
else:
    drop_at_pos(-350)

