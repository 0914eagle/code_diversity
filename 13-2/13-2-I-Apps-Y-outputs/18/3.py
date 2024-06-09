
def get_optimal_flavor(apples):
    # Sort the apples by their flavor
    apples.sort(key=lambda x: x[1])
    # Initialize the sum of the flavors
    total_flavor = 0
    # Loop through the apples and calculate the sum of the flavors
    for apple in apples:
        total_flavor += apple[1]
    # Return the sum of the flavors
    return total_flavor

def main():
    # Read the input
    N, L = map(int, input().split())
    # Create a list to store the apples
    apples = []
    # Loop through the apples and add them to the list
    for i in range(1, N+1):
        apples.append([i, L+i-1])
    # Get the optimal flavor
    optimal_flavor = get_optimal_flavor(apples)
    # Print the optimal flavor
    print(optimal_flavor)

if __name__ == '__main__':
    main()

