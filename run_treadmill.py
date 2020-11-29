#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary

def run_treadmill(crabot):
	crabot.gyro_reset()
	crabot.gyro_drive(400, 0, 3000)
	while crabot.gyro.angle() > 0:
		crabot.left_wheel.run(-100)
	crabot.left_wheel.stop()
	wait(1000)
	crabot.right_wheel.run_time(800, 3000)
	# crabot.gyro_drive_until_white(200, 0, "left")
	# crabot.gyro_turn(20, Direction.CLOCKWISE)
	# crabot.gyro_drive(200, 20, 300)
	# crabot.gyro_turn(-20, Direction.COUNTERCLOCKWISE)
	# crabot.gyro_drive(200, 0, 250)
	# wait(2000)
	crabot.bw_gyro_drive(-150, 0, -300)
	crabot.gyro_turn(-90, -90)
	crabot.gyro_reset()
	crabot.bw_gyro_drive(-150, 0, -250)

if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_treadmill(crabot)