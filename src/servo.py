# Библиотека для работы с сервоприводами
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(
    "WPI6", min_angle=0, max_angle=180, min_pulse_width=0.000544, max_pulse_width=0.0024
)

# Шаг сервопривода
step = 1

while True:
    for val in range(servo.min_angle, servo.max_angle, step):
        servo.angle = val
        sleep(0.02)
    for val in range(servo.max_angle, servo.min_angle, -step):
        servo.angle = val
        sleep(0.02)