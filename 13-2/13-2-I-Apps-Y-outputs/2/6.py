
def solve(n, temperatures):
    # Sort the temperatures in non-decreasing order
    temperatures.sort()
    # Initialize the rearranged temperatures list
    rearranged_temperatures = []
    # Loop through the temperatures and find the maximum difference between two consecutive temperatures
    for i in range(n-1):
        # Find the maximum difference between the ith and (i+1)th temperatures
        max_diff = max(abs(temperatures[i] - temperatures[i+1]), abs(temperatures[i+1] - temperatures[i]))
        # Add the temperature with the maximum difference to the rearranged temperatures list
        rearranged_temperatures.append(temperatures[i+1] if max_diff == abs(temperatures[i] - temperatures[i+1]) else temperatures[i])
    # Add the last temperature to the rearranged temperatures list
    rearranged_temperatures.append(temperatures[-1])
    # Return the rearranged temperatures list
    return rearranged_temperatures

