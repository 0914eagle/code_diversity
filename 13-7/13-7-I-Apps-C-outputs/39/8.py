
def get_treasure_map(N, M, K, map_string):
    # Initialize variables
    days = 0
    stamina = K
    treasure_reached = False
    current_location = (0, 0)
    visited_cells = set()
    treasure_location = (0, 0)
    
    # Parse the map string
    map = []
    for i in range(N):
        map.append(list(map_string[i * M:(i + 1) * M]))
    
    # Find the treasure location
    for i in range(N):
        for j in range(M):
            if map[i][j] == 'G':
                treasure_location = (i, j)
                break
    
    # Breadth-first search to find the shortest path to the treasure
    queue = [(current_location, stamina)]
    visited_cells.add(current_location)
    while queue:
        current_location, stamina = queue.pop(0)
        if current_location == treasure_location:
            treasure_reached = True
            break
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_location = (current_location[0] + i, current_location[1] + j)
            if 0 <= new_location[0] < N and 0 <= new_location[1] < M and new_location not in visited_cells:
                if map[new_location[0]][new_location[1]] in ['.', 'F', 'M']:
                    queue.append((new_location, stamina - 1))
                elif map[new_location[0]][new_location[1]] == '#':
                    queue.append((new_location, stamina))
        visited_cells.add(current_location)
        days += 1
        if days % 2 == 0 and days != 0:
            stamina = K
    
    # Return the result
    if treasure_reached:
        return days
    else:
        return -1

def main():
    N, M, K = map(int, input().split())
    map_string = [input() for _ in range(N)]
    print(get_treasure_map(N, M, K, map_string))

if __name__ == '__main__':
    main()

