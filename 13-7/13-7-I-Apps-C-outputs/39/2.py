
def get_treasure_map(N, M, K, map):
    # Initialize variables
    days = 0
    stamina = K
    visited = set()
    queue = [(0, 0)]

    # Direction vectors
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # Loop until the queue is empty
    while queue:
        # Get the current cell
        r, c = queue.pop(0)

        # Check if the cell has already been visited
        if (r, c) in visited:
            continue

        # Mark the cell as visited
        visited.add((r, c))

        # Check if the cell is the treasure
        if map[r][c] == 'G':
            return days

        # Get the cost of moving to the cell
        cost = 1 if map[r][c] == '.' else 2 if map[r][c] == 'F' else 3

        # Check if the stamina is enough to move to the cell
        if stamina < cost:
            # If not, camp and rest
            days += 1
            stamina = K

        # Update the stamina
        stamina -= cost

        # Add the neighboring cells to the queue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and map[nr][nc] != '#' and (nr, nc) not in visited:
                queue.append((nr, nc))

    # If the queue is empty and the treasure has not been found, return -1
    return -1

def main():
    # Read the input
    N, M, K = map(int, input().split())
    map = []
    for _ in range(N):
        map.append(input())

    # Get the treasure map
    days = get_treasure_map(N, M, K, map)

    # Print the output
    print(days)

if __name__ == '__main__':
    main()

