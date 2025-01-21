#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()

plat = MovablePlatform.first()
arm = RobotArm.first()

posSt = GPSWaypoint.find('StartOffset').get_location()
posOr = GPSWaypoint.find('Origin').get_location()
posDr = GPSWaypoint.find('DropOff').get_location()

dy = RangeFinder.find('C').get_distance()+posOr[1]-posSt[1]+0.2
dx = RangeFinder.find('B').get_distance()+posOr[0]-posSt[0]-1

plat.set_target_location(dx,dy,0)
sleep(1)
while plat.get_is_moving():
    sleep(0.5)
    
arm.set_grabber_location(1.2,0,0)
sleep(1)
while arm.get_is_moving():
    sleep(0.5)
arm.pickup()
sleep(0.5)
plat.set_target_location(posDr[0]-posSt[0]-1,posDr[1]-posSt[1],0)

#cleanup close code
SimEnv.disconnect()
