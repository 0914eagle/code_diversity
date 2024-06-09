
def get_not_connected_houses(n, m, connections):
    # Initialize a set to store the connected houses
    connected_houses = set()

    # Loop through the connections and add the connected houses to the set
    for connection in connections:
        connected_houses.add(connection[0])
        connected_houses.add(connection[1])

    # Find the houses that are not connected to the internet
    not_connected_houses = set(range(1, n + 1)) - connected_houses

    # Return the list of not connected houses
    return list(not_connected_houses)

def main():
    # Read the input
    n, m = map(int, input().split())
    connections = []
    for _ in range(m):
        connections.append(tuple(map(int, input().split())))

    # Call the function to get the not connected houses
    not_connected_houses = get_not_connected_houses(n, m, connections)

    # Check if all the houses are connected
    if len(not_connected_houses) == 0:
        print("Connected")
    else:
        # Print the not connected houses
        for house in not_connected_houses:
            print(house)

if __name__ == '__main__':
    main()

