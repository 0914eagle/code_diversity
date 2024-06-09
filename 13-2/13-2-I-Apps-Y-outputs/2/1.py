
def solve(n, temperatures):
    # Sort the temperatures in non-decreasing order
    temperatures.sort()
    # Initialize the rearranged temperatures list
    rearranged_temperatures = []
    # Loop through the temperatures and find the next temperature that satisfies the condition
    for i in range(n):
        # Find the next temperature that satisfies the condition
        next_temperature = next((temperature for temperature in temperatures[i:] if temperature > temperatures[i] + 1), None)
        # If no such temperature exists, return "impossible"
        if next_temperature is None:
            return "impossible"
        # Add the next temperature to the rearranged temperatures list
        rearranged_temperatures.append(next_temperature)
        # Remove the used temperature from the original temperatures list
        temperatures.remove(next_temperature)
    # Return the rearranged temperatures list
    return rearranged_temperatures

