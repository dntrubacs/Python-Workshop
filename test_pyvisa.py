# import pyvisa
import pyvisa

# initialize a resource manager
rm = pyvisa.ResourceManager()

# find all the resources available (devices connected to the computer)
all_device_adresses = rm.list_resources()

# go through each resource and return its device name
for device_adress in all_device_adresses:
    # try to establish a connection to the device
    try:
        device = rm.open_resource(device_adress)
        idn = device.query('*IDN?')
        print(f'Resource: {device_adress} is the device: {idn}')
    except:
        print(f'Resource: {device_adress} could not be opened')