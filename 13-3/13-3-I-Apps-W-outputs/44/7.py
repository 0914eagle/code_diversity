
def get_max_cuts(n, B, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    # Initialize the current cost to 0
    current_cost = 0
    # Loop through the array
    for i in range(n - 1):
        # Calculate the cost of the current cut
        cost = abs(a[i] - a[i + 1])
        # Check if the current cost is less than or equal to the budget
        if current_cost + cost <= B:
            # Increment the maximum number of cuts
            max_cuts += 1
            # Increment the current cost
            current_cost += cost
    # Return the maximum number of cuts
    return max_cuts

def main():
    # Read the input n and B
    n, B = map(int, input().split())
    # Read the array a
    a = list(map(int, input().split()))
    # Get the maximum number of cuts
    max_cuts = get_max_cuts(n, B, a)
    # Print the maximum number of cuts
    print(max_cuts)

if __name__ == '__main__':
    main()

