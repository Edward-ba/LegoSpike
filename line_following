from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

g_hub = PrimeHub()
g_right_sensor = ColorSensor('D')
g_motor_pair = MotorPair('A', 'E')
g_wheel_distance_apart = 14.5
g_wheel_radius = 4.25
g_wheel_circumference = 2 * math.pi * g_wheel_radius
g_motor_pair.set_motor_rotation(g_wheel_circumference, 'cm')
g_motor_pair.set_default_speed(-50)
g_motor_pair.set_stop_action('break')


def line_follow(hub, motor_pair, right_sensor, num):
    count = 0
    while count < num:
        if right_sensor.get_reflected_light() > 50:
            motor_pair.start_tank(-25, 15)
        else:
            motor_pair.start_tank(20, 15)
        count += 1


line_follow(g_hub, g_motor_pair, g_right_sensor, 200)
