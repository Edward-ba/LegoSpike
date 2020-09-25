from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

hub = PrimeHub()
motor_pair = MotorPair('A', 'E')
wheel_distance_apart = 14.5
wheel_radius = 4.25
wheel_circumference = 2 * math.pi * wheel_radius
motor_pair.set_motor_rotation(wheel_circumference, 'cm')

motor_pair.move_tank("""the amount to be in line with M06""", 'cm', left_speed=25, right_speed=25)
motor_pair.move_tank("""the amount to turn left 90 degrees""", 'cm', left_speed=-25, right_speed=25)
motor_pair.move_tank("""the amount past M06 and to the black line""", 'cm', left_speed=25, right_speed=25)
motor_pair.move_tank("""the amount to be in line with M07""", 'cm', left_speed=25, right_speed=25)
motor_pair.move_tank("""the amount to turn right 90 degrees""", 'cm', left_speed=25, right_speed=-25)
motor_pair.move_tank("""the amount to be on to of M07""", 'cm', left_speed=25, right_speed=25)
motor_pair.start_tank(25, -25)
