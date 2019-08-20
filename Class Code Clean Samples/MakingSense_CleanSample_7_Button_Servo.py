from gpiozero import LED, Button, DistanceSensor, Servo
from time import sleep

button = Button(16)
servo = Servo(18)

while True:
    
    if button.is_pressed == False:
        servo.max()
    else:
        servo.min()
