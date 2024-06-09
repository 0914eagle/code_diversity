
def get_not_connected_houses(n, m, connections):
    # Initialize a set to store the houses that are not connected to the internet
    not_connected_houses = set()
    
    # Iterate through the list of connections
    for connection in connections:
        # If the house is not already connected to the internet, add it to the set
        if connection not in not_connected_houses:
            not_connected_houses.add(connection)
    
    # Return the set of houses that are not connected to the internet
    return not_connected_houses

def main():
    # Read the number of houses and network cables from stdin
    n, m = map(int, input().split())
    
    # Read the list of connections from stdin
    connections = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Call the function to get the houses that are not connected to the internet
    not_connected_houses = get_not_connected_houses(n, m, connections)
    
    # Check if all the houses are connected to the internet
    if len(not_connected_houses) == 0:
        print("Connected")
    else:
        # Sort the set of houses and print them in increasing order
        for house in sorted(not_connected_houses):
            print(house)

if __name__ == '__main__':
    main()

