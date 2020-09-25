from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import math

g_hub = PrimeHub()
g_motor_pair = MotorPair('A', 'E')
g_front_motor = Motor('F')
g_wheel_distance_apart = 14.5
g_wheel_radius = 4.25
g_wheel_circumference = 2 * math.pi * g_wheel_radius
g_motor_pair.set_motor_rotation(g_wheel_circumference, 'cm')
g_front_motor.set_default_speed(40)


def flip(motor_pair, motor):
    turns = 0.35
    #    motor.run_for_rotations(turns)
    motor.run_for_rotations(-0.05)
    motor_pair.move_tank(22.5, 'cm', left_speed=-25, right_speed=10)
    motor_pair.move_tank(20, 'cm', left_speed=25, right_speed=25)


#    motor.run_for_rotations(-turns)

def to_mission(motor_pair):
    motor_pair.move_tank(35, 'cm', left_speed=25, right_speed=25)
    motor_pair.move_tank(2, 'cm', left_speed=25, right_speed=0)
    motor_pair.move_tank(7.5, 'cm', left_speed=25, right_speed=25)


# main code
# motor_pair.move_tank(35, 'cm', left_speed=25, right_speed=25)
to_mission(g_motor_pair)
flip(g_motor_pair, g_front_motor)

# motor_pair.move_tank(10.5, 'cm', left_speed=-25, right_speed=25)
# motor_pair.start_motor(25, 25)
