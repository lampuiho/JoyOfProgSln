from pyjop import *
SimEnv.connect()

arm = RobotArm.first()
arm.set_grabber_location([2,0.2,0])
sleep(2)
arm.pickup()
sleep(1)
arm.set_grabber_location([-10,0,2])
sleep(3)
arm.release()

#cleanup close code
SimEnv.disconnect()