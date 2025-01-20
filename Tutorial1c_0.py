# welcome to your first python script. This line starts with a #, meaning it is a comment for your benefit. Python ignores comments.
# the next two lines of code are always required, but can be ignored for the time being.
from pyjop import * 
SimEnv.connect()

#print hello world to the screen
print("Hello World")
#wait for 1 second
sleep(1)

# variable 'conv' pointing to the conveyor belt
conv = ConveyorBelt.find("_entityConveyorBelt0")
# set the speed of the conveyor belt (positive values are forwards, negative backwards, 0 means stop)
conv.set_target_speed(1)
