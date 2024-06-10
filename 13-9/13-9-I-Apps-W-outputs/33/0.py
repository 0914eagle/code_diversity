
import sys
input = sys.stdin.read()

def get_shortest_path(map, painter, hedgehogs, den):
    # Initialize the shortest path to infinity
    shortest_path = float('inf')
    
    # Initialize the queue with the starting position of the Painter and the three little hedgehogs
    queue = [(painter[0], painter[1], 0)]
    
    # Loop until the queue is empty
    while queue:
        # Get the current position, direction, and time from the queue
        pos, dir, time = queue.pop(0)
        
        # If the current position is the Beaver's den, update the shortest path and break
        if pos == den:
            shortest_path = time
            break
        
        # Get the neighbors of the current position
        neighbors = get_neighbors(map, pos, dir)
        
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not flooded and not a rock, add it to the queue
            if map[neighbor[0]][neighbor[1]] != '*' and map[neighbor[0]][neighbor[1]] != 'X':
                queue.append((neighbor[0], neighbor[1], time+1))
    
    # Return the shortest path
    return shortest_path

def get_neighbors(map, pos, dir):
    # Get the row and column of the current position
    row, col = pos
    
    # Initialize the neighbors list
    neighbors = []
    
    # Check if the current position is on the border
    if row == 0 or row == len(map)-1 or col == 0 or col == len(map[0])-1:
        # If the current position is on the border, add the neighbors that are not on the border
        if row > 0:
            neighbors.append((row-1, col))
        if row < len(map)-1:
            neighbors.append((row+1, col))
        if col > 0:
            neighbors.append((row, col-1))
        if col < len(map[0])-1:
            neighbors.append((row, col+1))
    else:
        # If the current position is not on the border, add all the neighbors
        neighbors.append((row-1, col))
        neighbors.append((row+1, col))
        neighbors.append((row, col-1))
        neighbors.append((row, col+1))
    
    # Return the neighbors list
    return neighbors

def main():
    # Get the input
    R, C = [int(x) for x in input().split()]
    map = [input().strip() for _ in range(R)]
    painter = [int(x) for x in input().split()]
    hedgehogs = [int(x) for x in input().split()]
    den = [int(x) for x in input().split()]
    
    # Get the shortest path
    shortest_path = get_shortest_path(map, painter, hedgehogs, den)
    
    # Print the output
    if shortest_path == float('inf'):
        print("KAKTUS")
    else:
        print(shortest_path)

if __name__ == '__main__':
    main()

