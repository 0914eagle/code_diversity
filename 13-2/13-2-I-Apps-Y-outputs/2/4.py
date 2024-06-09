
def solve(n, temperatures):
    # Sort the temperatures in non-decreasing order
    temperatures.sort()
    # Initialize the rearranged temperatures list
    rearranged_temperatures = []
    # Loop through the temperatures and find the maximum difference between consecutive temperatures
    for i in range(n-1):
        # Find the maximum difference between the ith and (i+1)th temperatures
        max_diff = max(temperatures[i+1] - temperatures[i], temperatures[n-1] - temperatures[i])
        # Add the ith temperature to the rearranged temperatures list
        rearranged_temperatures.append(temperatures[i])
        # Add the (i+1)th temperature to the rearranged temperatures list
        rearranged_temperatures.append(temperatures[i+1] + max_diff)
    # If the last temperature is not already in the rearranged temperatures list, add it
    if rearranged_temperatures[-1] != temperatures[n-1]:
        rearranged_temperatures.append(temperatures[n-1])
    return rearranged_temperatures
