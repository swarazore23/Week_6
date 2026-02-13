from machine import Pin
import time
pb2 = Pin(25, Pin.IN, Pin.PULL_UP)
counter = 0
while True:
    pb_val = pb2.value()
    if pb_val == 0:
        counter = counter - 1
        print (counter)
        
    time.sleep(0.2)