import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import define_operation_functions
from run_experiment import *
import serial
import time
from define_operation_functions import *
import Operations

# root window
root = tk.Tk()
root.title('Autosampler')
root.geometry('900x900')
root.resizable(True, True)

# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}
options_msg = {'padx': 15, 'pady': 15}

gdv_label = ttk.Label(frame, text='gDV:')
gdv_label.grid(column=0, row=1, sticky='W', **options)

ydv_label = ttk.Label(frame, text='yDV:')
ydv_label.grid(column=0, row=2, sticky='W', **options)

cell_sample_volume_label = ttk.Label(frame, text='cell sample volume:')
cell_sample_volume_label.grid(column=0, row=3, sticky='W', **options)

cell_sample_quench_label = ttk.Label(frame, text='cell quench volume:')
cell_sample_quench_label.grid(column=0, row=4, sticky='W', **options)

pri_pump_max_rate_label = ttk.Label(frame, text='pri pump max rate:')
pri_pump_max_rate_label.grid(column=0, row=5, sticky='W', **options)

port_cells_label = ttk.Label(frame, text='port of cells(Input Example: "1, 2, 3"): ')
port_cells_label.grid(column=0, row=6, sticky='W', **options)

port_air_label = ttk.Label(frame, text='port of air:')
port_air_label.grid(column=0, row=7, sticky='W', **options)

port_glycine_label = ttk.Label(frame, text='port of glycine:')
port_glycine_label.grid(column=0, row=8, sticky='W', **options)

port_wash_label = ttk.Label(frame, text='port of wash:')
port_wash_label.grid(column=0, row=9, sticky='W', **options)

setupPortValve_label = ttk.Label(frame, text='port for Valve:')
setupPortValve_label.grid(column=0, row=10, sticky='W', **options)

setupPortArm_label = ttk.Label(frame, text='port for Arm:')
setupPortArm_label.grid(column=0, row=11, sticky='W', **options)

ArmBaudRate_label = ttk.Label(frame, text='BaudRate for Arm:')
ArmBaudRate_label.grid(column=0, row=12, sticky='W', **options)

replica_label = ttk.Label(frame, text='Biological Replica Number(Input Example: "1, 2, 3"):')
replica_label.grid(column=0, row=13, sticky='W', **options)

time_point_label = ttk.Label(frame, text='Sampling Time Points(Input Example: "1, 2, 3"):')
time_point_label.grid(column=0, row=14, sticky='W', **options)

pump_label = ttk.Label(frame, text='Syringe Pump Start Time:')
pump_label.grid(column=0, row=15, sticky='W', **options)

quench_label = ttk.Label(frame, text='Quench Delay:')
quench_label.grid(column=0, row=16, sticky='W', **options)

gdv = tk.StringVar()
gdv_entry = ttk.Entry(frame, textvariable=gdv)
gdv_entry.insert(0, '2')
gdv_entry.grid(column=1, row=1, **options)
gdv_entry.focus()

ydv = tk.StringVar()
ydv_entry = ttk.Entry(frame, textvariable=ydv)
ydv_entry.insert(0, '3')
ydv_entry.grid(column=1, row=2, **options)
ydv_entry.focus()

cell_sample_volume = tk.StringVar()
cell_sample_volume_entry = ttk.Entry(frame, textvariable=cell_sample_volume)
cell_sample_volume_entry.insert(0, '5')
cell_sample_volume_entry.grid(column=1, row=3, **options)
cell_sample_volume_entry.focus()

cell_sample_quench = tk.StringVar()
cell_sample_quench_entry = ttk.Entry(frame, textvariable=cell_sample_quench)
cell_sample_quench_entry.insert(0, '2')
cell_sample_quench_entry.grid(column=1, row=4, **options)
cell_sample_quench_entry.focus()

pri_pump_max_rate = tk.StringVar()
pri_pump_max_rate_entry = ttk.Entry(frame, textvariable=pri_pump_max_rate)
pri_pump_max_rate_entry.insert(0, '75')
pri_pump_max_rate_entry.grid(column=1, row=5, **options)
pri_pump_max_rate_entry.focus()

port_cells = tk.StringVar()
port_cells_entry = ttk.Entry(frame, textvariable=port_cells)
port_cells_entry.insert(0, '8, 1, 2, 3, 4')
port_cells_entry.grid(column=1, row=6, **options)
port_cells_entry.focus()

port_air = tk.StringVar()
port_air_entry = ttk.Entry(frame, textvariable=port_air)
port_air_entry.insert(0, '5')
port_air_entry.grid(column=1, row=7, **options)
port_air_entry.focus()

port_glycine = tk.StringVar()
port_glycine_entry = ttk.Entry(frame, textvariable=port_glycine)
port_glycine_entry.insert(0, '6')
port_glycine_entry.grid(column=1, row=8, **options)
port_glycine_entry.focus()

port_wash = tk.StringVar()
port_wash_entry = ttk.Entry(frame, textvariable=port_wash)
port_wash_entry.insert(0, '7')
port_wash_entry.grid(column=1, row=9, **options)
port_wash_entry.focus()

setupPortValve = tk.StringVar()
setupPortValve_entry = ttk.Entry(frame, textvariable=setupPortValve)
setupPortValve_entry.insert(0, 'COM12')
setupPortValve_entry.grid(column=1, row=10, **options)
setupPortValve_entry.focus()

setupPortArm = tk.StringVar()
setupPortArm_entry = ttk.Entry(frame, textvariable=setupPortArm)
setupPortArm_entry.insert(0, 'COM14')
setupPortArm_entry.grid(column=1, row=11, **options)
setupPortArm_entry.focus()

ArmBaudRate = tk.StringVar()
ArmBaudRate_entry = ttk.Entry(frame, textvariable=ArmBaudRate)
ArmBaudRate_entry.insert(0, '19200')
ArmBaudRate_entry.grid(column=1, row=12, **options)
ArmBaudRate_entry.focus()

replica = tk.StringVar()
replica_entry = ttk.Entry(frame, textvariable=replica)
replica_entry.insert(0, '1, 2')
replica_entry.grid(column=1, row=13, **options)
replica_entry.focus()

time_point = tk.StringVar()
time_point_entry = ttk.Entry(frame, textvariable=time_point)
time_point_entry.insert(0, '0, 2, 5, 10, 15, 20, 30, 60, 120, 180, 240, 300')
time_point_entry.grid(column=1, row=14, **options)
time_point_entry.focus()

pump = tk.StringVar()
pump_entry = ttk.Entry(frame, textvariable=pump)
pump_entry.insert(0, '0')
pump_entry.grid(column=1, row=15, **options)
pump_entry.focus()

quench = tk.StringVar()
quench_entry = ttk.Entry(frame, textvariable=quench)
quench_entry.insert(0, '8')
quench_entry.grid(column=1, row=16, **options)
quench_entry.focus()


def valve_start_clicked():
    try:
        define_operation_functions.valve_startup()
    except AttributeError as error:
        showerror(title='Valve Start Up Error', message=error)
        return
    except serial.SerialException as serial_error:
        showerror(title='Valve Start Up Error', message=serial_error)
        return
    showinfo(title='Valve Start Up succeed', message='Starting Up Valve...')


valve_start_button = ttk.Button(frame, text='Valve Start Up')
valve_start_button.grid(column=0, row=17, **options)
valve_start_button.configure(command=valve_start_clicked)


def run_experiment_clicked():
    if gdv.get():
        gdv_input = int(gdv.get())
        define_operation_functions.gDV = gdv_input

    if ydv.get():
        ydv_input = int(ydv.get())
        define_operation_functions.yDV = ydv_input

    if cell_sample_volume.get():
        cell_sample_volume_input = int(cell_sample_volume.get())
        define_operation_functions.cell_sample_volume = cell_sample_volume_input

    if cell_sample_quench.get():
        cell_sample_quench_input = int(cell_sample_quench.get())
        define_operation_functions.cell_sample_quench = cell_sample_quench_input

    if pri_pump_max_rate.get():
        pri_pump_max_rate_input = int(pri_pump_max_rate.get())
        define_operation_functions.pri_pump_max_rate = pri_pump_max_rate_input

    if port_cells.get():
        port_cells_input = port_cells.get()
        tmp = [x.strip() for x in port_cells_input.split(',')]
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        define_operation_functions.port_cells = tmp

    if port_air.get():
        port_air_input = int(port_air.get())
        define_operation_functions.port_air = port_air_input

    if port_glycine.get():
        port_glycine_input = int(port_glycine.get())
        define_operation_functions.port_glycine = port_glycine_input

    if port_wash.get():
        port_wash_input = int(port_wash.get())
        define_operation_functions.port_wash = port_wash_input

    if setupPortValve.get():
        setupPortValve_input = setupPortValve.get()
        define_operation_functions.setupPortValve = setupPortValve_input

    if setupPortArm.get():
        setupPortArm_input = setupPortArm.get()
        define_operation_functions.setupPortArm = setupPortArm_input

    if ArmBaudRate.get():
        ArmBaudRate_input = int(ArmBaudRate.get())
        define_operation_functions.ArmBaudRate = ArmBaudRate_input

    if replica.get():
        replica_input = replica.get()
        tmp = [x.strip() for x in replica_input.split(',')]
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        run_experiment.biological_replica = tmp

    if time_point.get():
        time_point_input = time_point.get()
        tmp = [x.strip() for x in time_point_input.split(',')]
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        run_experiment.sampling_time_points = tmp

    if pump.get():
        pump_input = int(pump.get())
        run_experiment.syr_pump_time = pump_input

    if quench.get():
        quench_input = int(quench.get())
        run_experiment.qunech_delay = quench_input

    try:
        run_experiment_gui()
    except Exception as error:
        showerror(title='run experiment error', message=error)
        return


def run_experiment_gui():
    quench_time_points_gui = [x + qunech_delay for x in sampling_time_points]
    operation_table_gui = generate_operation_table_optimized(biological_replica, sampling_time_points,
                                                             quench_time_points_gui,
                                                             syr_pump_time)
    run_experiment_operation(operation_table_gui)


def delta_sleep(initial_time, s, replica, action, tube):
    """
    Parameters:
        s: seconds since elapsed to sleep until
    """
    if int(time.time()) > initial_time + s:
        # check if the delta time has already passed
        text_msg = 'Current Replica: ' + str(replica) + '\nCurrent Action: ' + str(
            action) + '\nCurrent Tube: ' \
                   + str(tube) + '\nEstimated time until the next action: 0 min(s)'
        msg = tk.Label(root, text=text_msg)
        msg.grid(column=0, row=17, columnspan=10, rowspan=4)
        root.update()

        msg.destroy()
    else:
        # find time needed to sleep to reach the specified param 's'
        needed_sleep = (initial_time + s) - int(time.time())

        # show info of time if there is no need to sleep
        if needed_sleep == 0:
            text_msg = 'Current Replica: ' + str(replica) + '\nCurrent Action: ' + str(
                action) + '\nCurrent Tube: ' \
                       + str(tube) + '\nEstimated time until the next action: 0 min(s)'
            msg = tk.Label(root, text=text_msg)
            msg.grid(column=0, row=17, columnspan=10, rowspan=4)
            root.update()

            msg.destroy()

        # update the status on gui every minute, sleep 60s per each loop until the needed_sleep equal to zero
        while needed_sleep > 0:
            if 0 < needed_sleep < 60:
                text_msg = 'Current Replica: ' + str(replica) + '\nCurrent Action: ' + str(
                    action) + '\nCurrent Tube: ' \
                           + str(tube) + '\nEstimated time until the next action: ' + str(
                    round(needed_sleep / 60)) + ' min(s)'
                msg = tk.Label(root, text=text_msg)
                msg.grid(column=0, row=17, columnspan=10, rowspan=4)
                root.update()
                time.sleep(needed_sleep)
                msg.destroy()
                return

            # print out current status on gui (updated per minute)
            text_msg = 'Current Replica: ' + str(replica) + '\nCurrent Action: ' + str(
                action) + '\nCurrent Tube: ' \
                       + str(tube) + '\nEstimated time until the next action: ' + str(
                round(needed_sleep / 60)) + ' min(s)'
            msg = tk.Label(root, text=text_msg)
            msg.grid(column=0, row=17, columnspan=10, rowspan=4)
            root.update()

            time.sleep(60)
            needed_sleep -= 60
            msg.destroy()


# Run experiment Operation
def run_experiment_operation(operation_table):
    initial_time = int(time.time())  # frame of reference in seconds
    for row in operation_table.itertuples():
        if row.action == "sampling":
            delta_sleep(initial_time, seconds(row.timedelay), row.replica, row.action, row.tube)
            sample_collection(row.replica, row.tube)
        elif row.action == "quenching":
            delta_sleep(initial_time, seconds(row.timedelay), row.replica, row.action, row.tube)
            sample_quench(row.tube)
        elif row.action == "syr_run":
            delta_sleep(initial_time, seconds(row.timedelay), row.replica, row.action, row.tube)

            if row.replica == 0:
                syr_pump_1.run(False)
            elif row.replica == 1:
                syr_pump_2.run(False)
            elif row.replica == 2:
                syr_pump_3.run(False)

    msg = tk.Label(root, text='Experiment Finished!')
    msg.grid(column=0, row=17, columnspan=10, rowspan=1)
    root.update()


run_experiment_button = ttk.Button(frame, text='Run Experiment')
run_experiment_button.grid(column=1, row=17, **options)
run_experiment_button.configure(command=run_experiment_clicked)


def end_wash_clicked():
    try:
        end_wash_gui()
    except Exception as error:
        showerror(title='end wash error', message=error)
        return
    showinfo(title='end wash started', message='end wash started...')


end_wash_button = ttk.Button(frame, text='End Wash')
end_wash_button.grid(column=2, row=17, **options)
end_wash_button.configure(command=end_wash_clicked)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()
