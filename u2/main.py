import eel
import os
from serial import Serial
from serial.tools import list_ports


def exit(page, sockets_still_open):
    Serial(PORT, BAUDRATE).close()
    os._exit(0)
    
    
@eel.expose
def get_data():
    with Serial(PORT, BAUDRATE) as ser:
        while True:
            try:
                line = ser.readline().decode('utf-8')
                return line
            except UnicodeDecodeError:
                pass
        

if __name__ == '__main__':
    ports:list = list_ports.comports()
    if len(ports) == 0:
        print('No device found')
        exit(1)
    else:
        PORT:str = ports[0].device
        BAUDRATE:int = 9600
        eel.init('web')
        eel.start('index.html', close_callback=exit)
