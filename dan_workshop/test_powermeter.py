# import pyvisa
import pyvisa

# initialize a resource manager
rm = pyvisa.ResourceManager()


# the resource name of the powermeter device connected to the computer
resource_name = 'USB0::0x1313::0x8078::P0018934::INSTR'

# open the device
powermeter = rm.open_resource(resource_name)

# read the current power value
power_value = powermeter.query('MEASure:POWer?')

# print the current power (default reading is in W)
print(f'The current power value is: {float(power_value)*1000} mW.')