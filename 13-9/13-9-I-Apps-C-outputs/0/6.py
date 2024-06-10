
def get_min_diff(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to infinity
    min_diff = float('inf')
    # Iterate over all possible combinations of batteries
    for i in range(len(batteries) - k + 1):
        # Get the first k batteries for the first chip
        chip1 = batteries[i:i + k]
        # Get the remaining batteries for the second chip
        chip2 = batteries[i + k:]
        # Calculate the difference in power outputs
        diff = max(chip1) - min(chip2)
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff

def main():
    # Read the input data
    n, k = map(int, input().split())
    batteries = list(map(int, input().split()))
    # Find the minimum difference
    min_diff = get_min_diff(n, k, batteries)
    # Print the result
    print(min_diff)

if __name__ == '__main__':
    main()

