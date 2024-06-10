
def get_manhattan_distance(p, q):
    r_p, c_p = p
    r_q, c_q = q
    return abs(r_p - r_q) + abs(c_p - c_q)

def find_tour(N, M):
    # Initialize the grid with the starting position
    grid = [[0] * M for _ in range(N)]
    grid[0][0] = 1

    # Initialize the current position
    current_position = (0, 0)

    # Initialize the visited squares
    visited = set()
    visited.add(current_position)

    # Initialize the tour
    tour = []

    # Loop until the entire grid is visited
    while len(visited) < N * M:
        # Get the current position
        current_row, current_col = current_position

        # Get the possible moves
        possible_moves = []
        if current_row > 0 and grid[current_row - 1][current_col] == 0:
            possible_moves.append((current_row - 1, current_col))
        if current_row < N - 1 and grid[current_row + 1][current_col] == 0:
            possible_moves.append((current_row + 1, current_col))
        if current_col > 0 and grid[current_row][current_col - 1] == 0:
            possible_moves.append((current_row, current_col - 1))
        if current_col < M - 1 and grid[current_row][current_col + 1] == 0:
            possible_moves.append((current_row, current_col + 1))

        # If there are no possible moves, return -1
        if not possible_moves:
            return -1

        # Choose the move with the minimum Manhattan distance
        minimum_distance = float("inf")
        for move in possible_moves:
            distance = get_manhattan_distance(current_position, move)
            if distance < minimum_distance:
                minimum_distance = distance
                next_position = move

        # Make the move
        grid[next_position[0]][next_position[1]] = 1
        visited.add(next_position)
        current_position = next_position
        tour.append(next_position)

    # If the entire grid is visited, return the tour
    return tour

def main():
    N, M = map(int, input().split())
    tour = find_tour(N, M)
    if tour == -1:
        print(-1)
    else:
        for row, col in tour:
            print(row, col)

if __name__ == '__main__':
    main()

