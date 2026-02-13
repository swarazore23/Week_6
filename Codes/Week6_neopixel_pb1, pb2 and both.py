from machine import Pin
import time
import neopixel

pb1 = Pin(23, Pin.IN, Pin.PULL_UP)
pb2 = Pin(25, Pin.IN, Pin.PULL_UP)
neo = neopixel.NeoPixel(Pin(33), 16)

i = 0

while True:
    pb1_val = pb1.value()
    pb2_val = pb2.value()
    
    if pb1_val == 0 and pb2_val == 0:
        i=0
        for i in range (0,16,1):
            neo[i] = (0,0,0)
            neo.write()
    
    elif pb1_val == 0:
        neo[i] = (255,0,0)
        neo.write()
        i=i+1
    
    elif pb2_val == 0:
        neo[i] = (0,0,0)
        neo.write()
        i=i-1
        

    time.sleep(0.2)