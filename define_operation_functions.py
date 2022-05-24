# parameters based on the experiment setup:
gDV = 2 # mL Round to mL
yDV = 3 # ml Round to mL
cell_sample_volume = 5 # mL ()
cell_quench_volume = 2 # mL ()
pri_pump_max_rate = 75 # mL/min
port_cells = [8, 1, 2, 3, 4]
port_air = 5
port_glycine = 6
port_wash = 7
_init_duration = 30 # min
min_PreP_rate = 0.01 # min rate
y_tube_block_rate =  max(min_PreP_rate, yDV/_init_duration)
y_tube_block_volume = _init_duration*y_tube_block_rate

from functions import *

XY_sample = 1
# Take_Cell_Samples
def Take_Cell_Samples(br,XY_sample):
 XY_valve = 1 # to sample tubes
 operation_function(port_cells[br],"INFUSE",pri_pump_max_rate,cell_sample_volume + (gDV+yDV),XY_valve,XY_sample)

# Flush Yellow Tube
def Flush_Yellow_Tube():
 XY_valve = 0 # to waste tube
 operation_function(port_air,"INFUSE",pri_pump_max_rate,(2*yDV),XY_valve,XY_sample)

# Back Flush Green Tube
def Back_Flush_Green_Tube(br):
 XY_valve = 0 # to waste tube
 operation_function(port_cells[br],"WITHDRAW",pri_pump_max_rate,(2*gDV),XY_valve,XY_sample)

# Wash Yellow Tube
def Wash_Yellow_Tube():
 XY_valve = 0 # to waste tube
 operation_function(port_wash,"INFUSE",pri_pump_max_rate,(3*yDV),XY_valve,XY_sample)

# Quench cell samples
def Quench_cell_samples(XY_sample):
 XY_valve = 1 # to sample tubes
 operation_function(port_glycine,"INFUSE",pri_pump_max_rate,cell_quench_volume+(yDV),XY_valve,XY_sample)

# Blocking Yellow Tube
def init_Block_Yellow_Tube():
 XY_valve = 0 # to waste tube
 operation_function(port_wash,"INFUSE",y_tube_block_rate,y_tube_block_volume,XY_valve,XY_sample)

# prime: fill wash and glycine inlet tubes
def init_Prime_Glycine_Wash_Tubes():
 XY_valve = 0 # to waste tube
 operation_function(port_glycine,"INFUSE",pri_pump_max_rate,(gDV),XY_valve,XY_sample)
 operation_function(port_wash, "INFUSE", pri_pump_max_rate, (gDV), XY_valve, XY_sample)


