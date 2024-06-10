
import sys

def get_shortest_time(map):
    # Initialize variables
    rows, cols = len(map), len(map[0])
    painter_pos, hedgehogs_pos = None, None
    time = 0
    queue = []

    # Find the painter and the hedgehogs' positions
    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 'D':
                den_pos = (r, c)
            elif map[r][c] == 'S':
                painter_pos = (r, c)
                hedgehogs_pos = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
                break

    # Breadth-first search to find the shortest path to the den
    queue.append((painter_pos, hedgehogs_pos, time))
    visited = set()
    while queue:
        current_pos, current_hedgehogs, current_time = queue.pop(0)
        if current_pos == den_pos:
            return current_time
        if current_pos in visited:
            continue
        visited.add(current_pos)
        for nr, nc in [(current_pos[0]+1, current_pos[1]), (current_pos[0]-1, current_pos[1]), (current_pos[0], current_pos[1]+1), (current_pos[0], current_pos[1]-1)]:
            if 0 <= nr < rows and 0 <= nc < cols and map[nr][nc] != 'X' and (nr, nc) not in visited:
                queue.append(((nr, nc), current_hedgehogs, current_time+1))
                if (nr, nc) in current_hedgehogs:
                    queue.append(((nr, nc), current_hedgehogs, current_time+1))
        for hedgehog in current_hedgehogs:
            if 0 <= hedgehog[0] < rows and 0 <= hedgehog[1] < cols and map[hedgehog[0]][hedgehog[1]] != 'X' and hedgehog not in visited:
                queue.append((hedgehog, current_hedgehogs, current_time+1))
                if hedgehog == den_pos:
                    return current_time+1

    return "KAKTUS"

def main():
    map = []
    for _ in range(int(input())):
        map.append(input())
    print(get_shortest_time(map))

if __name__ == '__main__':
    main()

