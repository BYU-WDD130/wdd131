def wind_chill(temperature, wind_speed):
    """Compute and return the wind chill factor as defuned by the US 
    National Weather Service.

    Parameters
        temperature: The air temperature in Fahrenheit at five feet
            above the ground.
        wind_speed: The spead of the wind in miles per hour at five feet 
            above the ground.
    Returns: The wind chill factor in degrees Fahrenheit.
    """
    chill_factor = 35.74 \
     + 0.6215 * temperature \
     - 35.75 * (wind_speed ** 0.16) \
     + 0.4275 * temperature * (wind_speed ** 0.16)
    rounded = round(chill_factor, 1)   
    return rounded

def heat_index(temperature, humidity):
     """Compute and return the heat index as defined by the US National Waether Service
    Parameters
        temperature: The air temperature in Fahrenheit at five feet
            above the ground.
        wind_speed: The spead of the wind in miles per hour at five feet 
            above the ground.
    Returns: The wind chill factor in degrees Fahrenheit.
    """