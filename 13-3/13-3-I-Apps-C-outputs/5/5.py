
def get_minimum_fuel(n, m, a, b):
    # Initialize the fuel variable
    fuel = 0
    
    # Loop through each planet
    for i in range(n):
        # Calculate the fuel needed for take-off from the current planet
        fuel_take_off = m // a[i]
        
        # Calculate the fuel needed for landing on the current planet
        fuel_landing = m // b[i]
        
        # Add the fuel needed for take-off and landing to the total fuel
        fuel += fuel_take_off + fuel_landing
    
    # Return the minimum fuel needed
    return fuel

