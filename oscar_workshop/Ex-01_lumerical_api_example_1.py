import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import time

# lumapi is NOT installed via pip. We must point Python to the installation folder.

# Common default paths
if sys.platform == 'win32':
    lumapi_path = r'C:\Program Files\ANSYS Inc\v252\Lumerical\api\python'
elif sys.platform == 'linux':
    lumapi_path = '/opt/lumerical/v232/api/python'
else:
    lumapi_path = '/Applications/Lumerical v232.app/Contents/API/Python'

if lumapi_path not in sys.path:
    sys.path.append(lumapi_path)

import lumapi

nw = lumapi.FDTD("nanowire_build_script.lsf")
nw.save("nanowire_test")
nw.run()
nw.feval("nanowire_plotcs.lsf")

end = False
while not end:
    input("Press enter to end")
    end = True

