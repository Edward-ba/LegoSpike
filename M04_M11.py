from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

g_hub = PrimeHub()
g_front_motor = Motor('F')
g_front_motor.set_default_speed(30)
g_back_motor = Motor('C')
g_back_motor.set_default_speed(30)
g_motor_pair = MotorPair('A', 'E')
g_wheel_distance_apart = 14.5
g_wheel_radius = 4.25
g_wheel_circumference = 2 * math.pi * g_wheel_radius
g_motor_pair.set_motor_rotation(g_wheel_circumference, 'cm')


def flip(hub, motor_pair, motor):
    turns = 0.35
    motor.run_for_rotations(-0.05)
    motor_pair.move_tank(22.5, 'cm', left_speed=-25, right_speed=10)


def to_mission(hub, motor_pair, front_motor, back_motor):
    motor_pair.move_tank(-35, 'cm', left_speed=25, right_speed=25)
    motor_pair.move_tank(2, 'cm', left_speed=25, right_speed=0)
    motor_pair.move_tank(-10, 'cm', left_speed=25, right_speed=25)


def go_home(hub, motor_pair, front_motor, back_motor):
    motor_pair.move_tank(-32, 'cm', left_speed=45, right_speed=25)


# main code
to_mission(g_hub, g_motor_pair, g_front_motor, g_back_motor)
flip(g_hub, g_motor_pair, g_front_motor)
go_home(g_hub, g_motor_pair, g_front_motor, g_back_motor)
