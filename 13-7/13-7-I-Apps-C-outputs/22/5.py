
def get_tolls(entrances, exits):
    # Initialize a dictionary to store the tolls for each exit
    tolls = {}
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # Calculate the toll for the current entrance and exit
        toll = abs(entrance - exit)
        # If the toll is already in the dictionary, update the value
        if toll in tolls:
            tolls[toll] += 1
        # Otherwise, add the toll to the dictionary with a count of 1
        else:
            tolls[toll] = 1
    # Return the sum of the tolls multiplied by the number of trucks
    return sum(toll * count for toll, count in tolls.items())

def get_min_tolls(entrances, exits):
    # Initialize the minimum tolls to 0
    min_tolls = 0
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance and exit are not the same, calculate the toll
        if entrance != exit:
            # Calculate the toll for the current entrance and exit
            toll = abs(entrance - exit)
            # Update the minimum tolls
            min_tolls += toll
    # Return the minimum tolls
    return min_tolls

def get_max_tolls(entrances, exits):
    # Initialize the maximum tolls to 0
    max_tolls = 0
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # Calculate the toll for the current entrance and exit
        toll = abs(entrance - exit)
        # Update the maximum tolls
        max_tolls = max(max_tolls, toll)
    # Return the maximum tolls
    return max_tolls

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
    # Calculate the minimum tolls
    min_tolls = get_min_tolls(entrances, exits)
    # Calculate the maximum tolls
    max_tolls = get_max_tolls(entrances, exits)
    # Print the minimum tolls
    print(min_tolls)
    # Print the maximum tolls
    print(max_tolls)

if __name__ == '__main__':
    main()

