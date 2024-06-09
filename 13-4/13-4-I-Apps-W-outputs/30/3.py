
def get_unconnected_houses(n, m, connections):
    # Initialize a set to store the connected houses
    connected_houses = set()

    # Loop through the connections and add the connected houses to the set
    for a, b in connections:
        connected_houses.add(a)
        connected_houses.add(b)

    # Find the unconnected houses by subtracting the connected houses from the total number of houses
    unconnected_houses = set(range(1, n + 1)) - connected_houses

    # Return the unconnected houses as a list
    return list(unconnected_houses)

def main():
    # Read the input
    n, m = map(int, input().split())
    connections = []
    for _ in range(m):
        a, b = map(int, input().split())
        connections.append((a, b))

    # Call the function to get the unconnected houses
    unconnected_houses = get_unconnected_houses(n, m, connections)

    # Print the output
    if not unconnected_houses:
        print("Connected")
    else:
        for house in sorted(unconnected_houses):
            print(house)

if __name__ == '__main__':
    main()

