import math
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

g_hub = PrimeHub()
g_front_motor = Motor('F')
g_front_motor.set_default_speed(35)
g_motor_pair = MotorPair('A', 'E')
wheel_distance_apart = 14.5
wheel_radius = 4.25
wheel_circumfrance = 2 * math.pi * wheel_radius
g_motor_pair.set_motor_rotation(wheel_circumfrance, 'cm')


def flip(motor_pair, motor):
    turns = 0.30
    motor.run_for_rotations(turns)
    motor.run_for_rotations(-turns)


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
    print ('Orientation', hub.motion_sensor.get_orientation())
    drive(hub, motor_pair, -60, 50)


def turn_test(hub, motor_pair):
    turn(hub, motor_pair, -90)
    print ('Orientation', hub.motion_sensor.get_orientation())
    turn(hub, motor_pair, 90)


# drive_test(g_hub, g_motor_pair)
#turn_test(g_hub, g_motor_pair)

def to_mission(hub, motor_pair, front_motor):
    drive(hub, motor_pair, 95, 25)
    turn(hub, motor_pair, -90)
    drive(hub, motor_pair, 50, 25)
    turn(hub, motor_pair, 50)
    drive(hub, motor_pair, 2.5, 10)
    drive(hub, motor_pair, -1, 10)
    turn(hub, motor_pair, -10)
    flip(motor_pair, front_motor)

    #to dance
    turn(hub, motor_pair, 65)
    turn(hub, motor_pair, -65)


    drive(hub, motor_pair, -30, 25)
    turn(hub, motor_pair, -90)
    front_motor.run_for_rotations(0.5)
    drive(hub, motor_pair, 15, 25)
    while True:
        turn(hub, motor_pair, 60)
        turn(hub, motor_pair, -60)


to_mission(g_hub, g_motor_pair, g_front_motor)
