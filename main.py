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
    
        
 
    open_claw()
            
    while not limit_sensor.pressed():
        # Rotate to the pick-up position.
        base_motor.run_angle(50, 25)
        print(base_motor.angle())
        

    print("robot calibrated")
    return base_motor.reset_angle(0)

def calibrate2():
    arm_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=None)
    arm_motor.run_angle(50,-25)
    open_claw()
    
    while not limit_sensor.pressed():
        # Rotate to the pick-up position.
         base_motor.run_angle(50, 25)
        print(base_motor.angle())
    

def pickup(pickup_position,elbow_taget,drop_pos_A,drop_pos_B,drop_pos_C,drop_pos_D,drop_pos_E):
    # Rotate to the pick-up position.
    base_motor = turn_motor
    base_motor.run_angle(60, pickup_position)

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
    if color_recognition() == Color.RED or color_recognition() == Color.BLUE or color_recognition() == Color.YELLOW or color_recognition() == Color.GREEN or color_recognition() == Color.WHITE:
        color = color_recognition()
        ev3.speaker.say((str(color).lower()).replace("color.", ""))
        if color == Color.RED:
            drop_at_pos(drop_pos_A)
        elif color == Color.BLUE:
            drop_at_pos(drop_pos_B)
        elif color == Color.GREEN:
            drop_at_pos(drop_pos_C)
        elif color == Color.YELLOW:
            drop_at_pos(drop_pos_D)
        elif color == Color.WHITE:
            drop_at_pos(drop_pos_E)
        else:
            elbow_motor
        print("YAAAAAAY")
        wait(5000)
    else:
        ev3.speaker.say("Nothing here!")
    wait(500)
    
def open_claw():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)

def color_recognition():
    return color_sensor.color()

def drop_at_pos(position):
    turn_motor.run_target(-100, position)
    arm_motor.run_target(-100, 25)
    open_claw()
    arm_motor.run_until_stalled(100)
    




# Write your program here.
drop_pos_A = 0
drop_pos_B = -150
drop_pos_C = -300
drop_pos_D = -450
drop_pos_E = -600
current_pos = 0


calibrate_arm()
for _ in range(240): # 240 iterations of 0.25s = 60s
    pickup(current_pos, -425, drop_pos_A, drop_pos_B, drop_pos_C, drop_pos_D, drop_pos_E)
    current_pos += 150
    if current_pos > 600:
        current_pos = 0
    wait(250) # wait for 0.25s

