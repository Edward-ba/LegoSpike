import math
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

# Set globals
g_hub = PrimeHub()
g_front_motor = Motor('F')
g_front_motor.set_default_speed(30)
g_back_motor = Motor('C')
g_back_motor.set_default_speed(50)
g_motor_pair = MotorPair('A', 'E')
g_wheel_distance_apart = 14.5
g_wheel_radius = 4.25
g_wheel_circumference = 2 * math.pi * g_wheel_radius
g_motor_pair.set_motor_rotation(g_wheel_circumference, 'cm')

# utility methods
def arm_move(hub, motor_pair, motor, amount):
    motor.run_for_rotations(amount)

def flip(hub, motor_pair, motor):
    amount = 0.25
    arm_move(hub, motor_pair, motor, amount)
    arm_move(hub, motor_pair, motor, -amount)

def drive(hub, motor_pair, dist, spd):
    motor_pair.move(dist, 'cm', steering=0, speed=spd)

# turns a robot a fixed angle
def turn(hub, motor_pair, angle_to_turn):
    if angle_to_turn != 0:
        print('AngleToTurn', angle_to_turn)
        fudge = 0.7
        rotate_const = 586.0 / 360.0

        hub.motion_sensor.reset_yaw_angle()
        turn_angle = rotate_const * angle_to_turn

        motor_pair.move(turn_angle, 'degrees', steering=100, speed=10)
        while True:
            yaw_angle = hub.motion_sensor.get_yaw_angle()

            if yaw_angle < 0 and angle_to_turn > 0:
                yaw_angle += 360
            elif yaw_angle > 0 and angle_to_turn < 0:
                yaw_angle -= 360

            print('Angle:', yaw_angle)
            error_angle = yaw_angle - angle_to_turn
            if error_angle >= 3:
                print('Error:', error_angle)
                motor_pair.move(-error_angle * rotate_const * fudge, 'degrees', steering=100, speed=10)
                yaw_angle = hub.motion_sensor.get_yaw_angle()
                print('Adj Angle:', yaw_angle)

            elif error_angle <= -3:
                print('Error:', error_angle)
                motor_pair.move(-error_angle * rotate_const * fudge, 'degrees', steering=100, speed=10)
                yaw_angle = hub.motion_sensor.get_yaw_angle()
                print('Adj Angle:', yaw_angle)
            else:
                break

def dump(hub, motor_pair, front_motor, back_motor):
    full = 0.7
    back_motor.run_for_rotations(-full)
    back_motor.run_for_rotations(full)


# do bocce Ball.
# 1. Get to Bocce ball court
def to_M08(hub, motor_pair, front_motor, back_motor):

    # Get to bocce ball court
    drive(hub, motor_pair, 97.5, 25)
    turn(hub, motor_pair, -91)
    drive(hub, motor_pair, 56.5, 30)

    # flip one piece into the court & setup for dump
    turn(hub, motor_pair, 70)
    arm_move(hub, motor_pair, front_motor, 0.2)
    drive(hub, motor_pair, 5, 10)
    drive(hub, motor_pair, -3, 10)
    arm_move(hub, motor_pair, front_motor, 0.30)
    arm_move(hub, motor_pair, front_motor, -0.20)

    drive(hub, motor_pair, -2, 10)
    turn(hub, motor_pair, 110)
    drive(hub, motor_pair, -7, 10)
    arm_move(hub, motor_pair, front_motor, 0.40)

    # dump remaining blocks
    dump(hub, motor_pair, front_motor, back_motor)


# move from Bocce ball to weights machine
def from_M08_to_M13(hub, motor_pair, front_motor, back_motor):

    # move from bocce ball to weight machine and slam into wall
    motor_pair.move(10, 'cm', steering=0, speed=25)
    turn(hub, motor_pair, -90)
    motor_pair.move(41, 'cm', steering=0, speed=25)
    turn(hub, motor_pair, -90)
    motor_pair.move(30, 'cm', steering=0, speed=25)

    # move back 3 cm and turn, pull down weight machine
    motor_pair.move(-3, 'cm', steering=0, speed=25)
    turn(hub, motor_pair, 90)
    motor_pair.move(6, 'cm', steering=0, speed=5)
    front_motor.run_for_rotations(-.75, 100)
    motor_pair.move(-3.5, 'cm', steering=0, speed=25)
    turn(hub, motor_pair, 90)
    motor_pair.move(-6, 'cm', steering=0, speed=25)
    front_motor.run_for_rotations(.75, 100)

def to_dance(hub, motor_pair, front_motor, back_motor):
    motor_pair.move(28, 'cm', steering=0, speed=30)
    turn(hub, motor_pair, 90)
    motor_pair.move(70, 'cm', steering=0, speed=40)
    turn(hub, motor_pair, 90)
    motor_pair.move(18, 'cm', steering=0, speed=35)
    motor_pair.move(180, 'degrees', steering=100, speed=25)
    front_motor.run_for_rotations(-.75, 100)

    while True:
        motor_pair.move(50, 'degrees', steering=100, speed=25)
        motor_pair.move(-50, 'degrees', steering=100, speed=25)


###### MAIN CODE ##############
# start the robot with the thing right of the right wheel lined up with the line to the left of the top of the white
# word CHALLENGE
# the back of the robot lined up with the line 1st from the thick black line
to_M08(g_hub, g_motor_pair, g_front_motor, g_back_motor)
from_M08_to_M13(g_hub, g_motor_pair, g_front_motor, g_back_motor)
to_dance (g_hub, g_motor_pair, g_front_motor, g_back_motor)
###### MAIN CODE ##############
# arm_move(g_hub, g_motor_pair, g_front_motor, 0.5)
# arm_move(g_hub, g_motor_pair, g_front_motor, -0.5)
# arm_move(g_hub, g_motor_pair, g_back_motor, 0.5)
# arm_move(g_hub, g_motor_pair, g_back_motor, -0.5)

# Old code
def to_dump(hub, motor_pair, front_motor, back_motor):
    turn(hub, motor_pair, 50)
    arm_move(hub, motor_pair, front_motor, 0.6)
    turn(hub, motor_pair, 90)
    drive(hub, motor_pair, -15, 10)

def drive_test(hub, motor_pair):
    drive(hub, motor_pair, 90, 50)
    print('Orientation', hub.motion_sensor.get_orientation())
    drive(hub, motor_pair, -60, 50)


def turn_test(hub, motor_pair):
    turn(hub, motor_pair, -90)
    print('Orientation', hub.motion_sensor.get_orientation())
    turn(hub, motor_pair, 90)
