
def get_tolls(entrances, exits):
    # Initialize a dictionary to store the tolls for each entrance
    tolls = {}
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been visited before, set the toll to 0
        if entrance not in tolls:
            tolls[entrance] = 0
        # Calculate the toll for the current entrance and exit
        toll = abs(entrance - exit)
        # Update the toll for the current entrance
        tolls[entrance] += toll
    # Return the sum of all tolls
    return sum(tolls.values())

def get_optimal_tolls(entrances, exits):
    # Initialize the optimal tolls to 0
    optimal_tolls = 0
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been visited before, set the toll to 0
        if entrance not in optimal_tolls:
            optimal_tolls[entrance] = 0
        # Calculate the toll for the current entrance and exit
        toll = abs(entrance - exit)
        # Update the toll for the current entrance
        optimal_tolls[entrance] += toll
    # Return the sum of all optimal tolls
    return sum(optimal_tolls.values())

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
    # Calculate the total tolls for the current arrangement
    current_tolls = get_tolls(entrances, exits)
    # Initialize the optimal tolls to 0
    optimal_tolls = 0
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been visited before, set the toll to 0
        if entrance not in optimal_tolls:
            optimal_tolls[entrance] = 0
        # Calculate the toll for the current entrance and exit
        toll = abs(entrance - exit)
        # Update the toll for the current entrance
        optimal_tolls[entrance] += toll
    # Return the sum of all optimal tolls
    return sum(optimal_tolls.values())

if __name__ == '__main__':
    print(main())

