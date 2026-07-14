# necessary libraries to be imported
import time as time
from matplotlib import pyplot as plt
from pm100d import PM100D



# initialize the powermeter and set the working wavelength to 635 nm
powermeter = PM100D()
powermeter.set_working_wavelength(wavelength=635)

# list to store all the powermeter readings
all_powermeter_readings = []

# list to store all the time readings
all_time_readings = []

# variable to control the while loop when running the experiment
experiment_running = True

# this function will stop the while loop where the experiment is running
def on_key_press(event):
    global experiment_running
    if event.key == "q":
        experiment_running = False


# turn on interactive mode for matplotlib
plt.ion()

# initialize the figure
fig, axis = plt.subplots(figsize=(12, 8))

# create an event such that
fig.canvas.mpl_connect("key_press_event", on_key_press)

# initialize a line for plotting (this will contain all the data - powermeter
# readings and time readings)
(powermeter_readings_line,) = axis.plot(
    [], [], markersize=0, color="red", label="Live power data"
)

# set the x and the y labels for the figure
axis.set_ylabel("Power (mW)")
axis.set_xlabel("Time (s)")
axis.set_title("Currently reading laser power over time. Press q to  "
               "stop it.")
axis.legend(loc="upper right")
axis.grid(True)

# start time of recording data
start_time = time.time()


# start the experiment
print('Start recording data!')
while experiment_running:

    # retrieve the current powermeter reading
    current_power = powermeter.get_current_power_reading()

    # save the powermeter reading
    all_powermeter_readings.append(current_power)

    # get the current time
    current_time = time.time() - start_time

    # save the current time
    all_time_readings.append(current_time)

    # plot the data
    powermeter_readings_line.set_data(all_time_readings,
                                      all_powermeter_readings)

    axis.relim()
    axis.autoscale_view()

    # redraw and flush
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.1)


# stop the plt interactive
plt.ioff()


# disconnect the device
powermeter.disconnect_device()
print('Stopped recording data!')

