
def get_optimal_allocation(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the optimal difference between the power outputs of the two chips as infinity
    d = float('inf')
    # Initialize the optimal allocation of batteries as an empty list
    allocation = []
    # Iterate over all possible combinations of batteries
    for i in range(len(batteries) - k + 1):
        # Get the current combination of batteries
        current_combination = batteries[i:i+k]
        # Get the power output of the first chip in the current combination
        power_output_1 = min(current_combination)
        # Get the power output of the second chip in the current combination
        power_output_2 = max(current_combination)
        # Calculate the difference between the power outputs of the two chips
        difference = power_output_2 - power_output_1
        # If the difference is less than or equal to the current optimal difference, update the optimal difference and allocation
        if difference <= d:
            d = difference
            allocation = current_combination
    # Return the optimal difference and allocation
    return d, allocation

def main():
    # Read the input data
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    # Get the optimal allocation of batteries
    d, allocation = get_optimal_allocation(n, k, batteries)
    # Print the optimal difference and allocation
    print(d)
    print(*allocation)

if __name__ == '__main__':
    main()

