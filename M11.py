from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()
motor_pair = MotorPair('A', 'E')
right_motor = Motor('E')
left_color = ColorSensor('B')
right_color = ColorSensor('D')
wheel_distance_apart = 14.5
wheel_radius = 4.25
wheel_circumference = 2 * math.pi * wheel_radius
motor_pair.set_motor_rotation(wheel_circumference, 'cm')
right_motor.set_default_speed(15)

i = 0
motor_pair.start_tank(25, 25)
while i < 200:
    if left_color.get_color() == 'black':
        print('l')
        motor_pair.start_tank(5, 25)
    elif right_color.get_color() == 'black':
        print('r')
        motor_pair.start_tank(25, 5)
    i += 1
motor_pair.stop()
motor_pair.move_tank(165, 'cm', left_speed=15, right_speed=15)
right_motor.run_for_rotations(20)
motor_pair.start_tank(-25, -25)
