
def get_connected_houses(n, m, connections):
    # Initialize a set to store the connected houses
    connected_houses = set()

    # Loop through the connections and add the connected houses to the set
    for a, b in connections:
        connected_houses.add(a)
        connected_houses.add(b)

    # Return the set of connected houses
    return connected_houses

def get_disconnected_houses(n, m, connections):
    # Get the set of connected houses
    connected_houses = get_connected_houses(n, m, connections)

    # Initialize a list to store the disconnected houses
    disconnected_houses = []

    # Loop through the houses and check if they are connected or not
    for i in range(1, n + 1):
        if i not in connected_houses:
            disconnected_houses.append(i)

    # Return the list of disconnected houses
    return disconnected_houses

def main():
    # Read the input
    n, m = map(int, input().split())
    connections = []
    for _ in range(m):
        a, b = map(int, input().split())
        connections.append((a, b))

    # Get the set of connected houses
    connected_houses = get_connected_houses(n, m, connections)

    # Check if all the houses are connected
    if len(connected_houses) == n:
        print("Connected")
    else:
        # Get the list of disconnected houses
        disconnected_houses = get_disconnected_houses(n, m, connections)

        # Print the list of disconnected houses
        for house in disconnected_houses:
            print(house)

if __name__ == '__main__':
    main()

