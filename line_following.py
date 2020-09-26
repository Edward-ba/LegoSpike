from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()
color = ColorSensor('D')
left = Motor('A')
right = Motor('E')
door_bell = ForceSensor('B')
motor_pair = MotorPair('A', 'E')
wheel_distance_apart = 14.5
wheel_radius = 4.25
wheel_circumference = 2 * math.pi * wheel_radius
motor_pair.set_motor_rotation(wheel_circumference, 'cm')
motor_pair.set_default_speed(-50)
count = 0

while count < 200:
    if door_bell.is_pressed():
        left.stop()
        right.stop()
        break

    if color.get_reflected_light() > 50:
        left.start_at_power(-25)
        right.start_at_power(15)
    else:
        right.start_at_power(20)
        left.start_at_power(15)

motor_pair.move(25.4, 'cm')