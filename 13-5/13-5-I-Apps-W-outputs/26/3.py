
def get_min_cost(costs, adjacency_list):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop through all possible starting points
    for start in range(len(costs)):
        # Calculate the minimum cost to catch the mouse starting from this point
        cost = get_min_cost_starting_from(start, costs, adjacency_list)
        
        # Update the minimum cost if necessary
        if cost < min_cost:
            min_cost = cost
    
    return min_cost

def get_min_cost_starting_from(start, costs, adjacency_list):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop through all possible next rooms
    for next_room in adjacency_list[start]:
        # Calculate the minimum cost to catch the mouse starting from this next room
        cost = get_min_cost_starting_from(next_room, costs, adjacency_list)
        
        # Update the minimum cost if necessary
        if cost < min_cost:
            min_cost = cost
    
    # Return the minimum cost plus the cost of setting a trap in the current room
    return min_cost + costs[start]

def main():
    # Read the input
    n = int(input())
    costs = list(map(int, input().split()))
    adjacency_list = [[] for _ in range(n)]
    for i in range(n):
        adjacency_list[i] = list(map(int, input().split()))
    
    # Calculate the minimum cost to catch the mouse
    min_cost = get_min_cost(costs, adjacency_list)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

