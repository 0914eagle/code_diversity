
def get_optimal_allocation(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the optimal allocation with the first k batteries
    optimal_allocation = batteries[:k]
    # Initialize the minimum difference between the power outputs of the two chips
    min_diff = 0
    for i in range(k, len(batteries)):
        # Add the ith battery to the optimal allocation
        optimal_allocation.append(batteries[i])
        # Calculate the power output of the first chip
        power_output_1 = sum(optimal_allocation[:k])
        # Calculate the power output of the second chip
        power_output_2 = sum(optimal_allocation[k:])
        # Calculate the difference between the power outputs of the two chips
        diff = abs(power_output_1 - power_output_2)
        # Update the minimum difference if necessary
        if diff < min_diff or min_diff == 0:
            min_diff = diff
    return min_diff

def main():
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    print(get_optimal_allocation(n, k, batteries))

if __name__ == '__main__':
    main()

