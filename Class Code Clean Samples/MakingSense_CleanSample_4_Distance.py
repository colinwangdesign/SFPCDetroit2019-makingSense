from gpiozero import LED, Button
from time import sleep

led = LED(21)
button = Button(16)

button.when_pressed = led.off
button.when_released = led.on
