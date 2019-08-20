from gpiozero import LED, Button
from time import sleep

led = LED(21)
button = Button(16)

button.when_pressed = led.off
button.when_released = led.on

#while True:
#    if button.is_pressed:
#        led.off()
#    else:
#        led.on()