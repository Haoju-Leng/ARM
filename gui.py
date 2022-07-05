import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import define_operation_functions
import Operations
import run_experiment
import serial

# root window
root = tk.Tk()
root.title('Autosampler')
root.geometry('700x600')
root.resizable(True, True)


# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

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

port_cells_label = ttk.Label(frame, text='port of cells:')
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

gdv = tk.StringVar()
gdv_entry = ttk.Entry(frame, textvariable=gdv)
gdv_entry.grid(column=1, row=1, **options)
gdv_entry.focus()

ydv = tk.StringVar()
ydv_entry = ttk.Entry(frame, textvariable=ydv)
ydv_entry.grid(column=1, row=2, **options)
ydv_entry.focus()

cell_sample_volume = tk.StringVar()
cell_sample_volume_entry = ttk.Entry(frame, textvariable=cell_sample_volume)
cell_sample_volume_entry.grid(column=1, row=3, **options)
cell_sample_volume_entry.focus()

cell_sample_quench = tk.StringVar()
cell_sample_quench_entry = ttk.Entry(frame, textvariable=cell_sample_quench)
cell_sample_quench_entry.grid(column=1, row=4, **options)
cell_sample_quench_entry.focus()

pri_pump_max_rate = tk.StringVar()
pri_pump_max_rate_entry = ttk.Entry(frame, textvariable=pri_pump_max_rate)
pri_pump_max_rate_entry.grid(column=1, row=5, **options)
pri_pump_max_rate_entry.focus()

port_cells = tk.StringVar()
port_cells_entry = ttk.Entry(frame, textvariable=port_cells)
port_cells_entry.grid(column=1, row=6, **options)
port_cells_entry.focus()

port_air = tk.StringVar()
port_air_entry = ttk.Entry(frame, textvariable=port_air)
port_air_entry.grid(column=1, row=7, **options)
port_air_entry.focus()

port_glycine = tk.StringVar()
port_glycine_entry = ttk.Entry(frame, textvariable=port_glycine)
port_glycine_entry.grid(column=1, row=8, **options)
port_glycine_entry.focus()

port_wash = tk.StringVar()
port_wash_entry = ttk.Entry(frame, textvariable=port_wash)
port_wash_entry.grid(column=1, row=9, **options)
port_wash_entry.focus()

setupPortValve = tk.StringVar()
setupPortValve_entry = ttk.Entry(frame, textvariable=setupPortValve)
setupPortValve_entry.grid(column=1, row=10, **options)
setupPortValve_entry.focus()

setupPortArm = tk.StringVar()
setupPortArm_entry = ttk.Entry(frame, textvariable=setupPortArm)
setupPortArm_entry.grid(column=1, row=11, **options)
setupPortArm_entry.focus()

ArmBaudRate = tk.StringVar()
ArmBaudRate_entry = ttk.Entry(frame, textvariable=ArmBaudRate)
ArmBaudRate_entry.grid(column=1, row=12, **options)
ArmBaudRate_entry.focus()


# convert butto


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
valve_start_button.grid(column=0, row=13, **options)
valve_start_button.configure(command=valve_start_clicked)


def run_experiment_clicked():
    if gdv.get():
        gdv_input = int(gdv.get())  # TODO: float or int
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

    if port_cells.get():  # TODO: add instruction later(input form etc.)
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
        setupPortValve_input = int(setupPortValve.get())
        define_operation_functions.setupPortValve = setupPortValve_input

    if setupPortArm.get():
        setupPortArm_input = int(setupPortArm.get())
        define_operation_functions.setupPortArm = setupPortArm_input

    if ArmBaudRate.get():
        ArmBaudRate_input = int(ArmBaudRate.get())
        define_operation_functions.ArmBaudRate = ArmBaudRate_input

    try:
        run_experiment.run_experiment_gui()
    except Exception as error:
        showerror(title='run experiment error', message=error)
        return
    showinfo(title='running experiment', message='Running experiment...')


run_experiment_button = ttk.Button(frame, text='Run Experiment')  # TODO: run experiment variable???
run_experiment_button.grid(column=1, row=13, **options)
run_experiment_button.configure(command=run_experiment_clicked)


def end_wash_clicked():
    try:
        run_experiment.end_wash_gui()
    except Exception as error:
        showerror(title='end wash error', message=error)
        return
    showinfo(title='end wash started', message='end wash started...')


end_wash_button = ttk.Button(frame, text='End Wash')
end_wash_button.grid(column=2, row=13, **options)
end_wash_button.configure(command=end_wash_clicked)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()
