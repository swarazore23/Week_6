from machine import Pin, PWM
import time

my_pwm = PWM(Pin(26, Pin.OUT))
my_pwm.freq(50)

while True:
    my_pwm.duty(25)
    time.sleep(0.2)
    my_pwm.duty(125)
    time.sleep(0.2)
