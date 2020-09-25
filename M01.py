from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

g_hub = PrimeHub()
g_motor_pair = MotorPair('A', 'E')
g_wheel_distance_apart = 14.5
g_wheel_radius = 4.25
g_wheel_circumference = 2 * math.pi * g_wheel_radius
g_motor_pair.set_motor_rotation(g_wheel_circumference, 'cm')


def to_mission(motor_pair):
    motor_pair.move_tank(65, 'cm', left_speed=25, right_speed=25)  # drive to the replay logo


def go_home(motor_pair):
    motor_pair.start_tank(-25, -25)


to_mission(g_motor_pair)
go_home(g_motor_pair)
