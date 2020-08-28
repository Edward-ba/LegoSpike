from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub()
drive_pair = MotorPair('A', 'E')
right_moter = Motor('E')
left_motor = Motor('A')
right_sensor = ColorSensor('F')
left_sensor = ColorSensor('B')

def go_until_black(hub, drive_pair):

    drive_pair.start(0, 30)
    while True:
        right_color = right_sensor.get_color()
        left_color = left_sensor.get_color()

        if right_color == 'black':
            right_moter.stop()
        if left_color == 'black':
            left_motor.stop()
        if right_color == 'black' and left_color == 'black':
            drive_pair.stop()
            return

go_until_black(hub, drive_pair)