#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

# In this tutorial you need to combine what you learned in the previous two tutorials:
# iterate all conveyor belts, check each belt if it is transporting something or not and then set the speed > 0 if (and only if) that is True
forward = 1
for belt in ConveyorBelt.find_all():
    if belt.get_is_transporting():
        belt.set_target_speed(10*forward)
        forward *= -1

#cleanup close code
SimEnv.disconnect()