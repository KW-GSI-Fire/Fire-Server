import os
import signal
from fastapi import FastAPI
from dotenv import load_dotenv

from status.serial import serial_reader

from routes.api import api


# Setting - dotenv
load_dotenv()

# Setting - serial
port = os.getenv('ARDUINO_SERIAL_PORT')
baud = os.getenv('ARDUINO_SERIAL_BAUD')

# Setting - remote
use_remote = False


# Run Serial Reader
serialThread = serial_reader.SerialReaderThread(port, baud, use_remote)
signal.signal(signal.SIGINT, serialThread.handler_exit)
serialThread.setDaemon(True)
serialThread.start()


# FastAPI APP
app = FastAPI()

# Middlewares - Routers
app.include_router(api.router)
