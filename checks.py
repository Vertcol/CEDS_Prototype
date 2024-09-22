"""
Returns 0.0-1.0 value estimating the likelyhood of a cable breach
context - information about the cable/environment
instrument_data - t.b.d
"""
def checkMeasurement(instrument_data: dict, context: dict) -> float:
    return 0.0

"""
Checks whether light is within tolerances within a given context
"""
def checkLight(instrument_data: dict, context: dict) -> str:
    # Calculate expected light
    cable_len = context['cable_length']
    cable_light = context['cable_light']
    expected_light = cable_len * cable_light

    # Check if real light is within tolerances
    light = instrument_data['light']
    light_delta = abs(light - expected_light)

    threshold = 14.0
    if light_delta > threshold:
        return f"Expected light of ~{expected_light} lumen, got {light} lumen. Delta exceeds threshold of {threshold} lumen"
    
    return None

"""
Checks whether temperature is within tolerances within a given context
"""
def checkTemperature(instrument_data: dict, context: dict) -> str:
    # Calculate expected temperature
    cable_len = context['cable_length']
    cable_temperature = context['cable_temperature']
    expected_temperature = context['cable_temperature']

    # Check if real temperature is within tolerances
    temperature = instrument_data['temperature']
    temperature_delta = abs(temperature - expected_temperature)

    threshold = 3.0
    if temperature_delta > threshold:
        return f"Expected temperature of ~{expected_temperature} °C, got {temperature} °C. Delta exceeds threshold of {threshold} °C"
    
    return None

"""
Checks whether resistance is within tolerances within a given context
"""
def checkResistance(instrument_data: dict, context: dict) -> str:
    # Calculate expected resistance
    cable_len = context['cable_length']
    cable_resistance = context['cable_resistance']
    expected_resistance = cable_len * cable_resistance

    # Check if real resistance is within tolerances
    resistance = instrument_data['resistance']
    resistance_delta = abs(resistance - expected_resistance)

    threshold = 3.0
    if resistance_delta > threshold:
        return f"Expected resistance of ~{expected_resistance} Ω, got {resistance} Ω. Delta exceeds threshold of {threshold} Ω"
    
    return None

"""
Checks whether voltage is within tolerances within a given context
"""
def checkVoltage(instrument_data: dict, context: dict) -> str:
    # Calculate expected resistance
    expected_cable_voltage = context['cable_voltage']

    # Check if real resistance is within tolerances
    cable_voltage = instrument_data['voltage']
    voltage_delta = abs(cable_voltage - expected_cable_voltage)

    threshold = 1.0
    if voltage_delta > threshold:
        return f"Expected resistance of ~{expected_cable_voltage}v, got {cable_voltage}v. Delta exceeds threshold of {threshold}v"
    
    return None