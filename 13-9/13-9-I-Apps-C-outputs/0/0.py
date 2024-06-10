
def get_power_outputs(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the power outputs for each chip
    power_outputs = [0] * n
    # Assign the batteries to the chips
    for i in range(n):
        power_outputs[i] = batteries[i * k]
    return power_outputs

def get_difference(power_outputs):
    # Calculate the difference between the power outputs of the two chips
    difference = abs(power_outputs[0] - power_outputs[1])
    for i in range(2, len(power_outputs)):
        difference = max(difference, abs(power_outputs[i] - power_outputs[i - 1]))
    return difference

def get_optimal_allocation(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the optimal difference
    optimal_difference = 1000000000
    # Iterate over all possible allocations of the batteries
    for i in range(n):
        for j in range(i + 1, n):
            # Get the power outputs for the two chips
            power_outputs = get_power_outputs(n, k, batteries[i * k:j * k])
            # Calculate the difference between the power outputs
            difference = get_difference(power_outputs)
            # Update the optimal difference
            optimal_difference = min(optimal_difference, difference)
    return optimal_difference

def main():
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    print(get_optimal_allocation(n, k, batteries))

if __name__ == '__main__':
    main()

