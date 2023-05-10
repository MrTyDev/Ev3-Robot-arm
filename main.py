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


color_positions = {
    "Color.RED": -150, 
    "Color.BLUE": -150,
    "Color.WHITE": -300,
    "Color.YELLOW": -450,
    "Color.GREEN": -600
}

def calibrate2(elbow_taget):
    arm_motor.run_until_stalled(75, then=Stop.HOLD, duty_limit=None)
    arm_motor.reset_angle(0)
    arm_motor.run_target(-75,elbow_taget)
    print("Calibrated")
    # Raise the arm to lift the wheel stack.
    
    open_claw()
    
    while not touch_sensor.pressed():
        # Rotate to the pick-up position.
        turn_motor.run_angle(50, 25)
        
        #print(turn_motor.angle())
    turn_motor.reset_angle(0)

def pickup(pickup_position,elbow_taget):

    # Rotate to the pick-up position.
    base_motor = turn_motor
    base_motor.run_angle(60, pickup_position)
    
    ev3.speaker.say("Waiting 5 seconds before pick up")
    wait(5000)

    # Lower the arm.
    elbow_motor = arm_motor
    elbow_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=50)

    # Close the gripper to grab the wheel stack.
    gripper_motor = claw_motor
    gripper_motor.reset_angle(0)
    gripper_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=100)
    print("Gripper angle: "+str(gripper_motor.angle()))
    if gripper_motor.angle() >= 110 :
        gripper_motor.run_angle(100,-100)
     
        
    # Raise the arm to lift the wheel stack.
    elbow_motor.reset_angle(0)
    elbow_motor.run_target(-100, elbow_taget)
    print("Color reflection: "+str(color_sensor.reflection()))    
    if color_sensor.reflection() > 10 and color_sensor.reflection() < 20:
        gripper_motor.run_angle(100,-100)
    #print(base_motor.angle())
    wait(500)
    if str(color_recognition()) in color_positions:
        color = color_recognition()
        ev3.speaker.say((str(color).lower()).replace("color.", ""))
        
        drop_at_pos(color_positions[str(color)], elbow_taget)
        
        wait(500)
    else:
        ev3.speaker.say("Nothing here!")

    
def open_claw():
    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200, -90)

def color_recognition():
    return color_sensor.color()

def drop_at_pos(position,elbow_taget):
    turn_motor.run_target(-100, position)
    arm_motor.run_target(-100, 25)
    open_claw()
     # Raise the arm to lift the wheel stack.
    arm_motor.run_target(-100, elbow_taget)
    




# Write your program here.
current_pos = 0


calibrate2(-800)
for l in range(3):
    for i in [0, 0, 0, 0, 0]:

       #print(turn_motor.angle())
       #print(current_pos)
        current_pos = i - turn_motor.angle()

        pickup(current_pos, -510)


        #print(turn_motor.angle())
        wait(250) # wait for 0.25s

