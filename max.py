import serial
import threading
import time

class DMXSender:
    def __init__(self, port="/dev/ttyS0", num_channels=512):
        self.serial = serial.Serial(port, baudrate=250000, stopbits=2)
        self.dmx_data = [0] * num_channels
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._send_dmx)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _send_dmx(self):
        while self.running:
            self.serial.break_condition = True
            time.sleep(0.0001)  # Break time
            self.serial.break_condition = False
            self.serial.write(bytearray([0] + self.dmx_data))  # Start code + data
            time.sleep(0.023)  # 44 Hz DMX refresh rate

    def set_channel(self, channel, value):
        if 0 <= channel < len(self.dmx_data):
            self.dmx_data[channel] = max(0, min(255, value))