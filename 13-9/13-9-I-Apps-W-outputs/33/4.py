
import sys

def get_shortest_time(map):
    # Initialize variables
    rows, cols = len(map), len(map[0])
    painter_pos, hedgehogs_pos = None, None
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = []

    # Find the painter and the hedgehogs' positions
    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 'S':
                hedgehogs_pos = (r, c)
            elif map[r][c] == 'D':
                painter_pos = (r, c)

    # Mark the starting position as visited
    visited[painter_pos[0]][painter_pos[1]] = True

    # Enqueue the starting position
    queue.append(painter_pos)

    # Loop through the queue
    while queue:
        # Dequeue a position
        pos = queue.pop(0)

        # If the position is the destination, return the distance
        if pos == hedgehogs_pos:
            return painter_pos[0] * cols + painter_pos[1]

        # Get the neighbors of the current position
        neighbors = get_neighbors(pos, rows, cols, map)

        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited, mark it as visited and enqueue it
            if not visited[neighbor[0]][neighbor[1]]:
                visited[neighbor[0]][neighbor[1]] = True
                queue.append(neighbor)

    # If the queue is empty, return -1
    return -1

def get_neighbors(pos, rows, cols, map):
    # Initialize the neighbors list
    neighbors = []

    # Get the row and column of the current position
    row, col = pos

    # Loop through the four possible directions
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            # If the neighbor is within the bounds of the map and is not a rock, add it to the neighbors list
            if 0 <= r < rows and 0 <= c < cols and map[r][c] != 'X':
                neighbors.append((r, c))

    return neighbors

def main():
    # Read the input
    rows, cols = [int(i) for i in input().split()]
    map = [input() for _ in range(rows)]

    # Get the shortest time
    time = get_shortest_time(map)

    # Print the output
    if time == -1:
        print("KAKTUS")
    else:
        print(time)

if __name__ == '__main__':
    main()

