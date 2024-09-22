import time
import asyncio
import importlib
import os
import numpy as np 
from instrument import Instrument, find_serial_port
from checks import checkLight, checkTemperature

"""
Collects data from an instrument
instrument_data - t.b.d
"""
def readInstruments() -> dict:
    time.sleep(0.5)
    return {
        "resistance": 4.63,
        "earth_voltage": 0.04,
        "voltage": 398
    }
    
"""
Construct a cable context
"""
def getContext() -> dict:
    return {
        'cable_name': 'Underground Segment #251',
        'cable_length': 20.2,
        'cable_resistance': 1.24,
        'cable_light': 0,
        'cable_temperature': 20,
        'cable_age': 2,
        'cable_voltage': 398
    }

checks = [
    checkLight,
    checkTemperature
]

"""
Core program loop
context - information about the cable/environment
instrument_data - t.b.d
"""
async def server():
    print("Waiting for instrument connection...")
    serial_port = find_serial_port()
    instrument = Instrument(serial_port.device)
    await instrument.connect()


    while True:
        print("INFO: Reading instrument data")
        instrument_data = await instrument.measure()
        context = getContext()

        # Run checks on data
        for check in checks:
            result = check(instrument_data, context)
            if result is None:
                print(f"INFO: Check {check.__name__} succeeded")
            else:
                print(f"INFO: Check {check.__name__} failed")
                print(result)

        time.sleep(2)

if __name__ == "__main__":
    while True:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(server())