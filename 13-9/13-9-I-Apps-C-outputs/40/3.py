
import math

def get_chance_of_success(N, L, walk, graph):
    # Initialize the chance of success to 1
    chance = 1
    
    # Loop through each room in the walk
    for i in range(L):
        # Get the current room and its neighbors
        current_room = walk[i]
        neighbors = graph[current_room]
        
        # Loop through each neighbor of the current room
        for neighbor in neighbors:
            # If the neighbor is not part of the walk, update the chance of success
            if neighbor not in walk[:i] and neighbor not in walk[i+1:]:
                chance *= 0.5
    
    # Return the chance of success
    return chance

def main():
    # Read the input
    N, L = map(int, input().split())
    walk = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for i in range(N):
        n, *neighbors = map(int, input().split())
        graph[i] = neighbors
    
    # Compute the chance of success
    chance = get_chance_of_success(N, L, walk, graph)
    
    # Print the result
    print(chance)

if __name__ == '__main__':
    main()

