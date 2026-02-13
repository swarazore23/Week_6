# Import the Pin class so we can work with GPIO pins of the ESP32
from machine import Pin
# (Ask yourself: which module handles hardware pins?)

# Import the time module
import time
# Create a push button object
# - Choose the correct GPIO pin number
# - Configure it as an INPUT
# - Enable the internal pull-up resistor
pb1 = Pin(23, Pin.IN, Pin.PULL_UP)
# (Think: what value will the button give when pressed?)
counter = 0
# Create a variable to store the counter value & Start counting from zero
# (Think: Why should this be outside the while loop?)
while True:
# Start an infinite loop so the ESP32 keeps checking the button
    pb_val = pb1.value()
    # Read the current state of the push button & Store the value (0 or 1) in a variable
    if pb_val == 0:
        counter = counter + 1
    # Check if the button is pressed
    # Remember: with PULL_UP, pressed means logic LOW (0)
        print (counter)
        # Increase the counter value by 1
    time.sleep(0.2)
        # Display the updated counter value(This helps us verify that the counter is working)
        
    # Add a small delay to Prevents multiple counts for one press & Slows down execution for readabilityfrom machine import Pin
