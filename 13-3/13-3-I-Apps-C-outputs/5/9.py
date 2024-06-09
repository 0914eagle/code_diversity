
def get_minimum_fuel(n, m, a, b):
    # Initialize the fuel amount to 0
    fuel = 0
    # Loop through each planet
    for i in range(n):
        # Calculate the fuel needed for takeoff from the current planet
        takeoff_fuel = m // a[i]
        # Calculate the fuel needed for landing on the current planet
        landing_fuel = m // b[i]
        # Add the fuel needed for takeoff and landing to the total fuel amount
        fuel += takeoff_fuel + landing_fuel
        # Update the mass of the rocket with fuel
        m -= takeoff_fuel * a[i] + landing_fuel * b[i]
    # Return the minimum fuel amount needed
    return fuel

