
def get_optimal_allocation(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Iterate over all possible combinations of batteries for each chip
    for i in range(len(batteries) - k + 1):
        for j in range(i + 1, len(batteries) - k + 1):
            # Calculate the difference between the power outputs of the two chips
            diff = abs(batteries[i + k - 1] - batteries[j + k - 1])
            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff
    # Return the minimum difference
    return min_diff

def main():
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    print(get_optimal_allocation(n, k, batteries))

if __name__ == '__main__':
    main()

