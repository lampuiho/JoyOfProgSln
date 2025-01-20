# welcome to your first python scripts. This line starts with a #, meaning it is a comment for your benefit. Python ignores comments.
# the next two lines of code are always required, but can be ignored for the time being.
from pyjop import * 
SimEnv.connect()

# variable pointing to the conveyor belt
conv = ConveyorBelt.find("_entityConveyorBelt0")

# set the speed of the conveyor belt (positive values are forwards, negative backwards)
conv.set_target_speed(1.5) #feel free to increase this!

# variable pointing to the delivery container.
container = DeliveryContainer.find("_entityDeliveryContainer0")

# open the delivery door and wait a few seconds for the barrel to arrive
container.open_door()
sleep(18) # after 18 seconds the barrel should've arrived

# close the door
container.close_door()
# wait until it is completely shut (takes about 7 seconds)
sleep(7)
# then deliver the barrel inside the container
container.deliver()
