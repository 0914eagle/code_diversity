
def get_tolls(entrances, exits):
    # Initialize a dictionary to store the tolls for each entrance
    tolls = {}
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance is not in the dictionary, add it with the toll for that exit
        if entrance not in tolls:
            tolls[entrance] = abs(exit - entrance)
        # If the entrance is already in the dictionary, update the toll if the current exit is cheaper
        else:
            tolls[entrance] = min(tolls[entrance], abs(exit - entrance))
    # Return the sum of the tolls for all entrances
    return sum(tolls.values())

def get_cheapest_tolls(entrances, exits):
    # Initialize a dictionary to store the tolls for each entrance
    tolls = {}
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance is not in the dictionary, add it with the toll for that exit
        if entrance not in tolls:
            tolls[entrance] = abs(exit - entrance)
        # If the entrance is already in the dictionary, update the toll if the current exit is cheaper
        else:
            tolls[entrance] = min(tolls[entrance], abs(exit - entrance))
    # Return the sum of the tolls for all entrances
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
    # Calculate the total tolls for the current setup
    total_tolls = get_tolls(entrances, exits)
    # Calculate the cheapest tolls possible by exchanging tickets
    cheapest_tolls = get_cheapest_tolls(entrances, exits)
    # Print the cheapest tolls
    print(cheapest_tolls)

if __name__ == '__main__':
    main()

