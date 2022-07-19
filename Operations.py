from define_operation_functions import *
import time

# operation blocks to perform sample collection and quench at each time point

# pre-setup before each experiment

def experiment_preparation():
    valve_startup()
    init_Block_Yellow_Tube()  # takes ~45 minutes
    init_Prime_Glycine_Wash_Tubes()
    Wash_Yellow_Tube()
    Flush_Yellow_Tube()


# sample operation
def sample_collection(br, XY_sample):
    Take_Cell_Samples(br, XY_sample)
    Flush_Yellow_Tube()
    Back_Flush_Green_Tube(br)
    Wash_Yellow_Tube()
    Flush_Yellow_Tube()


# Quench operation
def sample_quench(XY_sample):
    Quench_cell_samples(XY_sample)
    Wash_Yellow_Tube()
    Flush_Yellow_Tube()


# Run experiment Operation
def run_experiment(operation_table):
    initial_time = int(time.time())  # frame of reference in seconds
    for row in operation_table.itertuples():
        # global replica_num
        #replica_num = row.replica
        global action
        action = row.action
        global time_delay
        time_delay = row.timedelay
        global tube_num
        tube_num = row.tube

        if row.action == "sampling":
            delta_sleep(initial_time, seconds(row.timedelay))
            sample_collection(row.replica, row.tube)
        elif row.action == "quenching":
            delta_sleep(initial_time, seconds(row.timedelay))
            sample_quench(row.tube)
        elif row.action == "syr_run":
            delta_sleep(initial_time, seconds(row.timedelay))
            if row.replica == 0:
                syr_pump_1.run(False)
            elif row.replica == 1:
                syr_pump_2.run(False)
            elif row.replica == 2:
                syr_pump_3.run(False)


# End washing operation
def end_wash(biological_replica):
    XY_valve = 0  # to waste tube
    for i in range(len(biological_replica)):
        operation_function(port_cells[i], "INFUSE", pri_pump_max_rate, 10, XY_valve, XY_sample)
        operation_function(port_cells[i], "WITHDRAW", pri_pump_max_rate, 10, XY_valve, XY_sample)
        time.sleep(5)
        operation_function(port_cells[i], "INFUSE", pri_pump_max_rate, 10, XY_valve, XY_sample)
        operation_function(port_cells[i], "WITHDRAW", pri_pump_max_rate, 10, XY_valve, XY_sample)
