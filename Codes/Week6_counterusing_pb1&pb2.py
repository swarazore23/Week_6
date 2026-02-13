from machine import Pin
import time
pb1 = Pin(23, Pin.IN, Pin.PULL_UP)
pb2 = Pin(25, Pin.IN, Pin.PULL_UP)
counter = 0
while True:
    pb1_val = pb1.value()
    pb2_val = pb2.value()
    
    if pb1_val == 0 and pb2_val == 0:
        counter = 0
        print (counter)
        
    elif pb1_val == 0:
        counter = counter + 1
        print (counter)
        
    elif pb2_val == 0:
        counter = counter - 1
        print (counter)
        
    time.sleep(0.2)