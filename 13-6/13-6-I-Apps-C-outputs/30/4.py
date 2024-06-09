
def f1(n, m, roads):
    # Initialize a dictionary to store the distance of each path
    distances = {}
    
    # Loop through each road
    for road in roads:
        # Get the start and end cities of the road
        start, end = road[0], road[1]
        # Get the length of the road
        length = road[2]
        
        # If the path has not been seen before, add it to the dictionary with the length as the value
        if (start, end) not in distances:
            distances[(start, end)] = length
        # If the path has been seen before, update the value if the length is smaller
        elif length < distances[(start, end)]:
            distances[(start, end)] = length
    
    # Return the dictionary of distances
    return distances

def f2(distances, q, transfers):
    # Initialize a list to store the costs of each transfer
    costs = []
    
    # Loop through each transfer
    for transfer in transfers:
        # Get the start and end cities of the transfer
        start, end = transfer[0], transfer[1]
        
        # Get the cost of the transfer by finding the smallest distance of any path between the cities
        cost = min(distances[(start, end)], distances[(end, start)])
        
        # Add the cost to the list of costs
        costs.append(cost)
    
    # Return the list of costs
    return costs

def main():
    # Read the input
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    q = int(input())
    transfers = [list(map(int, input().split())) for _ in range(q)]
    
    # Call f1 to get the dictionary of distances
    distances = f1(n, m, roads)
    
    # Call f2 to get the list of costs
    costs = f2(distances, q, transfers)
    
    # Print the costs
    for cost in costs:
        print(cost)

if __name__ == '__main__':
    main()

