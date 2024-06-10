
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
    # Return the sum of the tolls for all entrances
    return sum(tolls.values())

def get_min_tolls(entrances, exits):
    # Initialize a list to store the minimum tolls for each entrance
    min_tolls = [0] * len(entrances)
    # Iterate over the entrances and exits
    for entrance, exit in zip(entrances, exits):
        # If the entrance has not been seen before, add it to the list with a toll of 0
        if entrance not in min_tolls:
            min_tolls.append(0)
        # Update the minimum toll for the entrance by adding the absolute difference between the entrance and exit numbers
        min_tolls[entrance] += abs(entrance - exit)
    # Return the minimum tolls for all entrances
    return min_tolls

def get_exchange_tolls(entrances, exits, num_exchanges):
    # Initialize a list to store the minimum tolls for each entrance after exchanging tickets
    min_tolls = get_min_tolls(entrances, exits)
    # Iterate over the number of exchanges
    for _ in range(num_exchanges):
        # Find the entrance with the minimum toll
        min_entrance = min(min_tolls)
        # Find the exit with the minimum toll that is not the same as the entrance
        min_exit = min(exits, key=lambda x: abs(min_entrance - x))
        # Update the minimum tolls for the entrance and exit
        min_tolls[min_entrance] += abs(min_entrance - min_exit)
        min_tolls[min_exit] += abs(min_entrance - min_exit)
    # Return the minimum tolls for all entrances after exchanging tickets
    return min_tolls

def main():
    num_trucks = int(input())
    entrances = []
    exits = []
    for _ in range(num_trucks):
        entrance, exit = map(int, input().split())
        entrances.append(entrance)
        exits.append(exit)
    num_exchanges = int(input())
    min_tolls = get_exchange_tolls(entrances, exits, num_exchanges)
    print(sum(min_tolls))

if __name__ == '__main__':
    main()

