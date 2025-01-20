#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

platform = MovablePlatform.first()
#set_target_location to move platform above dumpster
#sleep until arrived
#rotate platform to drop barrel
platform.set_target_location(0,0,12)
sleep(3)
platform.set_target_location(-5,0,12)
sleep(3)
platform.set_target_rotation(50,0,0)

#cleanup close code
SimEnv.disconnect()