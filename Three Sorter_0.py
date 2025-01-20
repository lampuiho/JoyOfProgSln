from pyjop import *
SimEnv.connect()
env = SimEnvManager.first()

class TJunc:
    def __init__(self, beltFor: ConveyorBelt, beltSplit: ConveyorBelt, scanner: RangeFinder, tagBac: str, speed: int):
        self.beltFor = beltFor
        self.beltSplit = beltSplit
        self.scanner = scanner
        self.tagBac = tagBac
        self.speed = speed
        self.state = 4
    def update(self):
        curTag = self.scanner.get_rfid_tag()
        beltSptLoad = self.beltSplit.get_is_transporting()
        if self.state == 0:
            if curTag and curTag == self.tagBac:
                self.state = 2
        elif self.state == 1:
            if curTag and curTag != self.tagBac:
                self.state = 3
        elif self.state == 2:
            if not beltSptLoad:
                self.state = 1
        elif self.state == 3:
            if not beltSptLoad:
                self.state = 0
        elif self.state == 4:
            self.state = 0
        self.updateByState()
    # states:
    #  0: both belts running forward
    #  1: beltFor running forward, beltSplit backwards
    #  2: beltFor stops, beltSplit forwards
    #  3: beltFor stops, beltSplit backwards
    #  4: both belts stop
    def updateByState(self):
        spdFor = self.speed
        spdBac = self.speed
        if self.state == 1:
            spdBac *= -1
        elif self.state == 2:
            spdFor = 0
        elif self.state == 3:
            spdFor = 0
            spdBac *= -1
        self.beltFor.set_target_speed(spdFor)
        self.beltSplit.set_target_speed(spdBac)
spd = 10
belt0 = ConveyorBelt.find('belt0')
tJunc0 = TJunc(belt0, ConveyorBelt.find('belt1'), RangeFinder.find('scan0'), 'Barrel', spd)
tJunc1 = TJunc(ConveyorBelt.find('belt3'), ConveyorBelt.find('belt4'), RangeFinder.find('scan1'), 'Box', spd)
ConveyorBelt.find('belt2').set_target_speed(spd)
lastDropTime = env.get_sim_time()

while SimEnv.run_main():
    tJunc0.update()
    tJunc1.update()
    simtime = env.get_sim_time()
    if (lastDropTime + 5 <= simtime) and (not belt0.get_is_transporting()):
        ObjectSpawner.first().spawn()
        lastDropTime = simtime
SimEnv.disconnect()
