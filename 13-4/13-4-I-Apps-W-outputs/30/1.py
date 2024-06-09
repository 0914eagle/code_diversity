
def get_connected_houses(n, m, connections):
    # Initialize a set to store the connected houses
    connected_houses = set()

    # Loop through the connections and add the connected houses to the set
    for connection in connections:
        connected_houses.add(connection[0])
        connected_houses.add(connection[1])

    # Return the set of connected houses
    return connected_houses

def get_not_connected_houses(n, m, connections):
    # Get the set of connected houses
    connected_houses = get_connected_houses(n, m, connections)

    # Initialize a list to store the not connected houses
    not_connected_houses = []

    # Loop through the houses and check if they are connected or not
    for i in range(1, n + 1):
        if i not in connected_houses:
            not_connected_houses.append(i)

    # Return the list of not connected houses
    return not_connected_houses

def main():
    # Read the input
    n, m = map(int, input().split())
    connections = []
    for _ in range(m):
        a, b = map(int, input().split())
        connections.append((a, b))

    # Get the not connected houses
    not_connected_houses = get_not_connected_houses(n, m, connections)

    # Print the output
    if len(not_connected_houses) == 0:
        print("Connected")
    else:
        for house in sorted(not_connected_houses):
            print(house)

if __name__ == '__main__':
    main()

