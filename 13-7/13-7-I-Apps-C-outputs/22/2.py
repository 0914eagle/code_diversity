
def get_tolls(entrances, exits):
    # Initialize a dictionary to store the tolls for each entrance
    tolls = {}
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been seen before, add it to the dictionary with a toll of 0
        if entrance not in tolls:
            tolls[entrance] = 0
        # Update the toll for the entrance by adding the absolute difference between the entrance and exit numbers
        tolls[entrance] += abs(entrance - exit)
    # Return the sum of the tolls
    return sum(tolls.values())

def get_optimal_tolls(entrances, exits):
    # Initialize the optimal tolls to 0
    optimal_tolls = 0
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been seen before, add it to the dictionary with a toll of 0
        if entrance not in tolls:
            tolls[entrance] = 0
        # Update the toll for the entrance by adding the absolute difference between the entrance and exit numbers
        tolls[entrance] += abs(entrance - exit)
        # If the toll for the entrance is greater than the current optimal toll, update the optimal toll
        if tolls[entrance] > optimal_tolls:
            optimal_tolls = tolls[entrance]
    # Return the optimal tolls
    return optimal_tolls

def get_exchange_tolls(entrances, exits):
    # Initialize a dictionary to store the tolls for each entrance
    tolls = {}
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been seen before, add it to the dictionary with a toll of 0
        if entrance not in tolls:
            tolls[entrance] = 0
        # Update the toll for the entrance by adding the absolute difference between the entrance and exit numbers
        tolls[entrance] += abs(entrance - exit)
    # Return the sum of the tolls
    return sum(tolls.values())

def main():
    # Read the number of trucks
    n = int(input())
    # Read the entrances and exits for each truck
    entrances = []
    exits = []
    for i in range(n):
        entrance, exit = map(int, input().split())
        entrances.append(entrance)
        exits.append(exit)
    # Calculate the total tolls
    total_tolls = get_tolls(entrances, exits)
    # Calculate the optimal tolls
    optimal_tolls = get_optimal_tolls(entrances, exits)
    # Calculate the exchange tolls
    exchange_tolls = get_exchange_tolls(entrances, exits)
    # Print the total tolls, optimal tolls, and exchange tolls
    print(total_tolls)
    print(optimal_tolls)
    print(exchange_tolls)

if __name__ == '__main__':
    main()

