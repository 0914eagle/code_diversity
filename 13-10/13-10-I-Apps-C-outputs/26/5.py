
def get_manhattan_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def find_tour(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    tour = []
    current_pos = (0, 0)
    visited[0][0] = True
    tour.append(current_pos)
    while len(tour) < n * m:
        neighbors = []
        for i in range(max(current_pos[0] - 1, 0), min(current_pos[0] + 2, n)):
            for j in range(max(current_pos[1] - 1, 0), min(current_pos[1] + 2, m)):
                if not visited[i][j] and get_manhattan_distance(current_pos, (i, j)) in [2, 3]:
                    neighbors.append((i, j))
        if not neighbors:
            return -1
        current_pos = neighbors[0]
        visited[current_pos[0]][current_pos[1]] = True
        tour.append(current_pos)
    return tour

def main():
    n, m = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    print(find_tour(grid))

if __name__ == '__main__':
    main()

