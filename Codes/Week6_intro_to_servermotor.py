from machine import Pin, PWM
import time

my_pwm = PWM(Pin(26, Pin.OUT))
#we can also write above line as my_pwm = PWM(Pin(26, Pin.OUT),freq=50)
my_pwm.freq(50)
my_pwm.duty(35  )
time.sleep(2)
my_pwm.duty(77)


    
    
    
    










