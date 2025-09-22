

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²
WATER_DENSITY = 998.2  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s

# Function 1: Water column height
def water_column_height(tower_height, tank_height):
    return tower_height + 0.75 * tank_height

# Function 2: Pressure gain from water height
def pressure_gain_from_water_height(height):
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

# Function 3: Pressure loss from pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    if pipe_diameter == 0:
        return 0
    return -(friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2) / (2000 * pipe_diameter)

# Function 4: Pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return -(0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings) / 2000

# Function 5: Reynolds number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

# Function 6: Pressure loss from pipe reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    if fluid_velocity == 0:
        return 0.0
    if smaller_diameter == 0 or reynolds_number == 0:
        return 0.0  # safety against invalid input
    ratio_pow4_minus1 = (larger_diameter / smaller_diameter)**4 - 1
    k = (0.1 + 50.0 / reynolds_number) * ratio_pow4_minus1
    return -(k * WATER_DENSITY * fluid_velocity**2) / 2000.0

# Enhancement: Convert kPa to psi
def kpa_to_psi(kpa):
    return kpa * 0.145038

# Example main function
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    supply_pipe_length = float(input("Length of supply pipe from tank to lot (meters): "))
    num_fittings = int(input("Number of 90° angles in supply pipe: "))
    house_pipe_length = float(input("Length of pipe from supply to house (meters): "))

    # Simplified example
    water_height = water_column_height(tower_height, tank_height)
    pressure_gain = pressure_gain_from_water_height(water_height)
    pressure_loss_fittings = pressure_loss_from_fittings(1.65, num_fittings)
    pressure_at_house = pressure_gain + pressure_loss_fittings  # simplified, not full hydraulics

    print(f"Pressure at house: {pressure_at_house:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure_at_house):.1f} psi")

if __name__ == "__main__":
    main()