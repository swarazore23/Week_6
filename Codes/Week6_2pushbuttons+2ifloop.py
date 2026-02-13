from machine import Pin
import time
pb1 = Pin(23, Pin.IN, Pin.PULL_UP)
pb2 = Pin(34, Pin.IN, Pin.PULL_UP)

while True:
    pb1_value = pb1.value()
    pb2_value = pb2.value()
    
    if pb1_value == 0:
        print("only Button 1 pressed")
        
    if pb2_value == 0:
        print("only Button 2 pressed")
        
    time.sleep(0.2)