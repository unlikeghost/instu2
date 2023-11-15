import sys
import eel
from serial import Serial
from tkinter import messagebox
from serial.tools import list_ports


class EKG:
    def __init__(self, sampling_rate:int, samples:int, debug:bool=False, baudrate:int=9600):
        """Constructor method

        Args:
            sampling_rate (int): Iterations per second
            samples (int): How many samples of EKG you want to show
            debug (bool, optional): If you want to simulate the EKG. Defaults to False.
            baudrate (int, optional): Baudrate of the serial connection. Defaults to 9600. Deprecated if debug is True.
        """
        if not debug:
            ports:list = self.__check_ports__()
            if ports is not None:
                self.serial = Serial(ports[0].device, baudrate)
            else:
                messagebox.showerror('Error', 'No device found')
                sys.exit()
                        
        self.values:list = [0] * samples * sampling_rate
        self.debug:bool = debug

    def __check_ports__(self) -> list:
        """Check if there is any device connected to the computer. Deprecated if debug is True
        Returns:
            list: List of devices connected to the computer
        """
        ports:list = list_ports.comports()
        if len(ports) != 0:
            return ports
        else:
            return None
    
    def exit(self, *args, **kwargs):
        """Kill the program."""
        messagebox.showinfo('Exit', 'Closing connection.')
        if not self.debug:
            self.serial.close()
        sys.exit()
    
    def read_data(self) -> list:
        """Read the data from the serial port or simulate it if debug is True

        Returns:
            list: List of samples, each sample is a float.
        """
        if self.debug:
            value:float = random.randint(200, 500)
        else:
            value:float = float(self.serial.readline().decode('utf-8'))
        
        self.values.pop(0)
        self.values.append(value)
        
        return self.values

@eel.expose
def get_data() -> list:
    return ekg.read_data()

if __name__ == '__main__':
    
    DEBUG:bool = True
    if DEBUG:
        import random
    
    ekg = EKG(sampling_rate=100, samples=3, debug=DEBUG)
    
    eel.init('web')
    eel.start('index.html', mode='chrome', host='localhost', port=8274,
              close_callback=ekg.exit)