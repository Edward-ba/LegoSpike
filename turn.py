import math
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub()
drive_pair = MotorPair('A', 'E')

def turn(hub, drive_pair, angle_to_turn):

    if (angle_to_turn > 0 and angle_to_turn < 150) or (angle_to_turn < 0 and angle_to_turn > -150):

        print('AngleToTurn', angle_to_turn)
        fudge = 0.7;
        rotate_const = 586.0 / 360.0

        hub.motion_sensor.reset_yaw_angle()
        turn = rotate_const * angle_to_turn

        drive_pair.move(turn, 'degrees', steering=100, speed=30)
        yaw_angle = hub.motion_sensor.get_yaw_angle()
        print('Angle:', yaw_angle)

        error_angle = yaw_angle - angle_to_turn;
        iferror_angle >= 3:
            print('Error:', error_angle)
            drive_pair.move(-error_angle * rotate_const * fudge, 'degrees', steering=100, speed=10)
            yaw_angle = hub.motion_sensor.get_yaw_angle()
            print('Adj Angle:', yaw_angle)

        elif error_angle <= -3:
            print('Error:', error_angle)
            drive_pair.move(-error_angle * rotate_const * fudge, 'degrees', steering=100, speed=10)
            yaw_angle = hub.motion_sensor.get_yaw_angle()
            print('Adj Angle:', yaw_angle)


turn(hub, drive_pair, -130)
turn(hub, drive_pair, 130)

turn(hub, drive_pair, -90)
turn(hub, drive_pair, -90)
turn(hub, drive_pair, 45)
turn(hub, drive_pair, 45)
turn(hub, drive_pair, 45)
turn(hub, drive_pair, 45)