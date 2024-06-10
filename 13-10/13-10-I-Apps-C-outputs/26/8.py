
def get_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_tour(grid):
    n, m = len(grid), len(grid[0])
    visited = set()
    tour = []
    current_position = (0, 0)
    visited.add(current_position)
    tour.append(current_position)
    while len(visited) < n * m:
        neighbors = []
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and get_manhattan_distance(current_position, (i, j)) in [2, 3]:
                    neighbors.append((i, j))
        if not neighbors:
            return -1
        current_position = neighbors[0]
        visited.add(current_position)
        tour.append(current_position)
    return tour

def main():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(input().split())
    tour = find_tour(grid)
    if tour == -1:
        print(-1)
    else:
        for position in tour:
            print(position[0], position[1])

if __name__ == '__main__':
    main()

