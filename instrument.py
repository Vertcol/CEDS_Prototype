import time
import asyncio
import serial.tools.list_ports
import serial.serialutil
from serial_asyncio import open_serial_connection

class Instrument:
    def __init__(self, serial_device):
        self.serial_device = serial_device

    async def connect(self):
        self.serial_reader, self.serial_writer = await open_serial_connection(url=self.serial_device, baudrate=115200)
        self.serial_writer.write("CONNECT\n".encode())
        connect_response = await self.serial_reader.readline()
        print(f"INFO: Instrument connected ({connect_response})")

    
    async def measure(self) -> dict:
        self.serial_writer.write("READ\n".encode())
        measure_response = await self.serial_reader.readline()
        parts = measure_response.decode().split(';')

        instrument_data = {
            'light': float(parts[0]),
            'temperature': float(parts[1])
        }

        print(f"DEBUG: Instrument Data:\n {instrument_data}")

        return instrument_data


def find_serial_port():
    while True:
        time.sleep(0.2)
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "USB Serial Device" in port.description or "bit" in port.description:
                return port