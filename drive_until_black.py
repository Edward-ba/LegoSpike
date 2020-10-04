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


def go_until_black(hub, motor_pair):
    right_sensor = ColorSensor('F')
    left_sensor = ColorSensor('B')

    motor_pair.start(0, 30)
    while True:
        right_color = right_sensor.get_color()
        left_color = left_sensor.get_color()

        if right_color == 'black':
            motor_pair.stop()
            motor_pair.start_tank(left_speed=30, right_speed=-10)
            if left_color == 'black':
                motor_pair.stop()
        if left_color == 'black':
            motor_pair.stop()
            motor_pair.start_tank(left_speed=-10, right_speed=30)
            if right_color == 'black':
                motor_pair.stop()
        if right_color == 'black' and left_color == 'black':
            motor_pair.stop()
            break


go_until_black(g_hub, g_motor_pair)
