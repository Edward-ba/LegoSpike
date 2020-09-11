from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

g_hub = PrimeHub()
g_drive_pair = MotorPair('A', 'E')
wheel_distance_apart = 14.5
wheel_diameter = 4.25
wheel_circumference = 2 * math.pi * wheel_diameter
g_drive_pair.set_motor_rotation(wheel_circumference, 'cm')


def go_until_black(hub, drive_pair):
    right_sensor = ColorSensor('F')
    left_sensor = ColorSensor('B')

    drive_pair.start(0, 30)
    while True:
        right_color = right_sensor.get_color()
        left_color = left_sensor.get_color()

        if right_color == 'black':
            drive_pair.stop()
            drive_pair.start_tank(left_speed=30, right_speed=-10)
            if left_color == 'black':
                drive_pair.stop()
        if left_color == 'black':
            drive_pair.stop()
            drive_pair.start_tank(left_speed=-10, right_speed=30)
            if right_color == 'black':
                drive_pair.stop()
        if right_color == 'black' and left_color == 'black':
            drive_pair.stop()
            break


go_until_black(g_hub, g_drive_pair)