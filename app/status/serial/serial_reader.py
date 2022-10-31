from urllib.parse import uses_relative
import serial
import threading

from ..status_manager import writeStatus


class SerialReaderThread(threading.Thread):
    def __init__(self, port, baud, use_remote):
        self.port = port
        self.baud = baud
        self.use_remote = use_remote
        self.thread_exit = False

        threading.Thread.__init__(self, name='SerialReader')


    def handler_exit(self, signum, frame):
        self.thread_exit = True


    def parsing_data(self, data):
        raw = ''.join(data).strip()

        # print('[serial_reader_thread/parsing_data()] Successfully Parsed Data from Serial:', raw)
        writeStatus(raw, self.use_remote)


    def serialRead(self, ser):
        line = []

        while not self.thread_exit:
            readed = ser.read()

            for c in readed:
                line.append(chr(c))

                if c == 10: # NL
                    self.parsing_data(line)

                    del line[:]


    def run(self):
        # open serial
        ser = serial.Serial(self.port, self.baud, timeout=0)

        # start reading
        self.serialRead(ser)
