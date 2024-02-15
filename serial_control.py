import serial.tools.list_ports

class SerialControl():
    def __init__(self):
        self.data = 0
        self.coms = []
    def serial_com_list(self):
        ports = serial.tools.list_ports.comports()
        self.coms = [com[0] for com in ports]

    def serial_connect(self, port):
        try:
            self.ser.is_open
        except:
            self.ser = serial.Serial()
            self.ser.baudrate = 9600
            self.ser.port = port
            self.ser.timeout = 0.1

        try:
            if self.ser.is_open:
                print("Port is already opened")
                self.ser.status = True
            else:
                self.ser = serial.Serial()
                self.ser.baudrate = 9600
                self.ser.port = port
                self.ser.timeout = 0.01
                self.ser.open()
                self.ser.status = True
        except:
            self.ser.status = False

    def serial_close(self):
        try:
            self.ser.is_open
            self.ser.close()
            self.ser.status = False
        except:
            self.ser.status = False

    def serial_sync(self):
        data = self.ser.readline().decode().strip()
        self.ser.reset_input_buffer()
        return data
