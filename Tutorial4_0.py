from pyjop import *
SimEnv.connect()

# hints for this tutorial SimEnv:
# find_all conveyor belts and save them in a list
all_convs = ConveyorBelt.find_all()

# iterate all_convs with a for loop (unlock from Perks menu)
for conv in all_convs:
    # print name of each conveyor belt
    print(conv.entity_name)
    # set_target_speed of each conveyor belt to 5.0 in the next line
    conv.set_target_speed(10)
    
    
