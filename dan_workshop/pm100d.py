from pyThorlabsPM100x.driver import ThorlabsPM100x
import time


class PM100D:
    """
    High-level class used to control the Thorlabs PM100D power meter. This
    class is based pn the pyThorlabsPM100x driver. See their original
    repository for more information.


    Attributes:
        device_address: The MAC address of the device. If None is given, the
            computer will automatically connect to the first device found.
        device: ThorlabsPM100x object representing the low level driver
            used to communicate with the physical device.
    """

    def __init__(self, device_address: str = None):
        if device_address is None:
            addresses = ThorlabsPM100x().list_devices()
            self.device_address = addresses[0][0]
        else:
            self.device_address = device_address

        # connect to the powermeter
        self.device = ThorlabsPM100x()
        self.device.connect_device(device_addr=self.device_address)

    def disconnect_device(self) -> None:
        """Disconnects the powermeter."""
        self.device.disconnect_device()

    def get_current_power_reading(self) -> float:
        """Gets the current power reading.

        Returns:
            Float representing the power reading measured in mW.
        """
        return float(self.device.power[0]) * 1000

    def set_working_wavelength(self, wavelength: float) -> None:
        """Sets the powermeter working wavelength.

        Args:
            wavelength: Float representing the working wavelength of the
                powermeter (measured in nm).
        """
        # set the working wavelength
        self.device.wavelength = wavelength

    def retrieve_average_power_reading(
        self, time_delay: float = 1, samples: int = 3
    ) -> float:
        """Retrieves multiple power readings and averages them.

        Args:
            time_delay: The time delay between two consecutive readings.
            samples: Number of readings taken.
        """
        # average reading_power
        average_reading_power = 0
        for i in range(samples):
            average_reading_power += self.get_current_power_reading()
            # wait for the given time delay
            time.sleep(time_delay)

        # return the average power
        return average_reading_power / samples