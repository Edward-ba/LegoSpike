import math
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

g_hub = PrimeHub()
g_front_motor = Motor('F')
g_front_motor.set_default_speed(30)
g_back_motor = Motor('C')
g_back_motor.set_default_speed(15)
g_motor_pair = MotorPair('A', 'E')
g_wheel_distance_apart = 14.5
g_wheel_radius = 4.25
g_wheel_circumference = 2 * math.pi * g_wheel_radius
g_motor_pair.set_motor_rotation(g_wheel_circumference, 'cm')


def arm_move(hub, motor_pair, motor, amount):
    motor.run_for_rotations(amount)


def flip(hub, motor_pair, motor):
    amount = 0.25
    arm_move(hub, motor_pair, motor, amount)
    arm_move(hub, motor_pair, motor, -amount)


def drive(hub, motor_pair, dist, spd):
    motor_pair.move(dist, 'cm', steering=0, speed=spd)


def turn(hub, motor_pair, angle_to_turn):
    # if (angle_to_turn > 0 and angle_to_turn < 150) or (angle_to_turn < 0 and angle_to_turn > -150):
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


def drive_test(hub, motor_pair):
    drive(hub, motor_pair, 90, 50)
    print('Orientation', hub.motion_sensor.get_orientation())
    drive(hub, motor_pair, -60, 50)


def turn_test(hub, motor_pair):
    turn(hub, motor_pair, -90)
    print('Orientation', hub.motion_sensor.get_orientation())
    turn(hub, motor_pair, 90)


# drive_test(g_hub, g_motor_pair)
# turn_test(g_hub, g_motor_pair)

def to_mission(hub, motor_pair, front_motor, back_motor):
    drive(hub, motor_pair, 99, 24)
    turn(hub, motor_pair, -90)
    drive(hub, motor_pair, 56, 25)
    turn(hub, motor_pair, 70)
    arm_move(hub, motor_pair, front_motor, 0.2)
    drive(hub, motor_pair, 5, 10)
    drive(hub, motor_pair, -4, 10)
    arm_move(hub, motor_pair, front_motor, 0.3)
    arm_move(hub, motor_pair, front_motor, -0.5)
    turn(hub, motor_pair, 110)
    drive(hub, motor_pair, -7, 10)


def to_dump(hub, motor_pair, front_motor, back_motor):
    turn(hub, motor_pair, 50)
    arm_move(hub, motor_pair, front_motor, 0.6)
    turn(hub, motor_pair, 90)
    drive(hub, motor_pair, -15, 10)


def dump(hub, motor_pair, front_motor, back_motor):
    full = 0.7

    back_motor.run_for_rotations(-full)
    back_motor.run_for_rotations(full)


def to_dance(hub, motor_pair, front_motor, back_motor):
    drive(hub, motor_pair, 15, 10)
    turn(hub, motor_pair, 90)
    drive(hub, motor_pair, 30, 25)
    turn(hub, motor_pair, -90)
    drive(hub, motor_pair, -20, 25)
    arm_move(hub, motor_pair, -0.5)

    while True:
        turn(hub, motor_pair, 60)
        turn(hub, motor_pair, -60)


def to_rdump(hub, motor_pair, front_motor, back_motor):
    turn(hub, motor_pair, -90)
    front_motor.run_for_rotations(-0.5)
    turn(hub, motor_pair, -50)


# start the robot with the thing right of the right wheel lined up with the line to the left of the top of the white
# word CHALLENGE
# the back of the robot lined up with the line 1st from the thick black line

to_mission(g_hub, g_motor_pair, g_front_motor, g_back_motor)
dump(g_hub, g_motor_pair, g_front_motor, g_back_motor)
