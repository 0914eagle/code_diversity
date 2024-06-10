
def get_min_cost(citizens, target):
    
    # Sort the list of citizens in non-decreasing order
    citizens.sort()
    # Initialize the cost to 0
    cost = 0
    # Loop through the citizens and add the difference between their welfare and the target to the cost
    for i in range(len(citizens)):
        cost += abs(citizens[i] - target)
    return cost

def main():
    # Read the number of citizens and their welfare from stdin
    n = int(input())
    citizens = list(map(int, input().split()))
    # Calculate the target welfare as the average of the welfare of all citizens
    target = sum(citizens) // len(citizens)
    # Call the get_min_cost function to find the minimum cost required to equalize the welfare of all citizens
    cost = get_min_cost(citizens, target)
    # Print the minimum cost to stdout
    print(cost)

if __name__ == '__main__':
    main()

