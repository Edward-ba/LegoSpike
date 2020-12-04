from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

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


def dump(hub, back_motor):
    full = 0.75
    tiny = 0.10
    slow = 15
    fast = 60

    # tip contents slowly
    back_motor.set_default_speed(slow)
    back_motor.run_for_rotations(-full)

    # reset motor speed fast
    back_motor.set_default_speed(fast)

    # 3-shakes
    for x in range(3):
        back_motor.run_for_rotations(tiny)
        back_motor.run_for_rotations(-tiny)

    # get back to reset position
    back_motor.run_for_rotations(full)
    back_motor.set_default_speed(slow)


def arm_move(hub, motor_pair, motor, amount):
    motor.run_for_rotations(amount)


def flip(hub, motor_pair, motor):
    amount = 0.4
    arm_move(hub, motor_pair, motor, amount)
    arm_move(hub, motor_pair, motor, -amount)


def drive(hub, motor_pair, dist, spd):
    motor_pair.move(dist, 'cm', steering=0, speed=spd)


def drive_test(hub, motor_pair):
    drive(hub, motor_pair, 90, 50)
    print('Orientation', hub.motion_sensor.get_orientation())
    drive(hub, motor_pair, -60, 50)


def turn_test(hub, motor_pair):
    turn(hub, motor_pair, -90)
    print('Orientation', hub.motion_sensor.get_orientation())
    turn(hub, motor_pair, 90)


def to_mission(hub, motor_pair, front_motor, back_motor):
    drive(hub, motor_pair, 98, 24)
    turn(hub, motor_pair, -90)
    drive(hub, motor_pair, 47.5, 25)
    turn(hub, motor_pair, 75)
    turn(g_hub, g_motor_pair, 70)
    g_front_motor.run_for_rotations(.15, 50)
    drive(g_hub, g_motor_pair, 5, 25)
    drive(g_hub, g_motor_pair, -3, 25)
    g_front_motor.run_for_rotations(.3, 50)
    g_front_motor.run_for_rotations(-.45, 50)
    drive(g_hub, g_motor_pair, -2, 25)
    turn(g_hub, g_motor_pair, 115)
    drive(g_hub, g_motor_pair, -6, 25)
    g_front_motor.run_for_rotations(.75, 100)


def to_dump(hub, motor_pair, front_motor, back_motor):
    turn(hub, motor_pair, 50)
    arm_move(hub, motor_pair, front_motor, 0.6)
    turn(hub, motor_pair, 90)
    drive(hub, motor_pair, -15, 10)


def dump(hub, motor_pair, front_motor, back_motor):
    full = 0.7
    tiny = 0.1

    back_motor.run_for_rotations(-full)
    for x in range(3):
        arm_move(hub, motor_pair, back_motor, tiny)
        arm_move(hub, motor_pair, back_motor, -tiny)
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


# start the robot with the thing right of the right wheel lined up with the line to the left of the top of the white
# word CHALLENGE
# the back of the robot lined up with the line 1st from the thick black line

to_mission(g_hub, g_motor_pair, g_front_motor, g_back_motor)
to_dump(g_hub, g_motor_pair, g_front_motor, g_back_motor)
dump(g_hub, g_motor_pair, g_front_motor, g_back_motor)
to_dance(g_hub, g_motor_pair, g_front_motor, g_back_motor)

to_mission(g_hub, g_motor_pair, g_front_motor, g_back_motor)
dump(g_hub, g_motor_pair, g_front_motor, g_back_motor)

# Dump and move to M13 code
g_motor_pair.move(10, 'cm', steering=0, speed=25)
turn(g_hub, g_motor_pair, -90)
g_motor_pair.move(40, 'cm', steering=0, speed=25)
turn(g_hub, g_motor_pair, -90)
g_motor_pair.move(30, 'cm', steering=0, speed=25)
g_motor_pair.move(-3, 'cm', steering=0, speed=25)
turn(g_hub, g_motor_pair, 90)
g_motor_pair.move(1, 'cm', steering=0, speed=25)
g_motor_pair.move(7, 'cm', steering=0, speed=5)
g_front_motor.run_for_rotations(-.75, 100)
g_motor_pair.move(-10, 'cm', steering=0, speed=5)
g_front_motor.run_for_rotations(.75, 100)
turn(g_hub, g_motor_pair, 90)
g_motor_pair.move(20, 'cm', steering=0, speed=25)
