from pyjop import *
SimEnv.connect()

env = SimEnvManager.first()
env.reset()
sleep(0.1)

cr = AirliftCrane.find('crane')
ex = DataExchange.find("control_center")
cmds = ex.get_data('instruction_sets')
for cmd in cmds:
    picked = False
    x = 0
    y = 0
    xv = 0
    yv = 0
    for c in cmd:
        if c == 'L':
            y-=1
        elif c == 'R':
            y+=1
        elif c == 'F':
            x+=1
        elif c == 'B':
            x-=1
        elif not picked:
            picked = True
            xv = x
            yv = y
            x = 0
            y = 0
    if xv == -x and yv == -y:
        print(cmd, x, y)
        break;
cr.set_target_location(xv,yv,0)
sleep(0.1)
while cr.get_is_moving():
    sleep(0.1)
cr.pickup()
sleep(0.5)
cr.set_target_location(0,0,0)
sleep(0.1)
while cr.get_is_moving():
    sleep(0.1)
cr.release()
sleep(0.1)

SimEnv.disconnect()