from Operations import *
# perform sample collection and quench at all time points (user input)
biological_replica = [1, 2]
sampling_time_points = [0, 2, 5, 10, 15, 20, 30, 60, 120, 180, 240, 300] # min
syr_pump_time = 0 # assign the timepoint you want the syringe pump to start
qunech_delay = 8 # min

# system operations (no user input)
quench_time_points = [x + qunech_delay for x in sampling_time_points]
operation_table = generate_operation_table_optimized(biological_replica, sampling_time_points, quench_time_points, syr_pump_time)
experiment_preparation() # blocking and priming valves
valve_startup()
run_experiment(operation_table)
end_wash(biological_replica)



