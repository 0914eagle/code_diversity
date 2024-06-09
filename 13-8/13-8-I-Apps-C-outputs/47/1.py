
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    visited = [[False] * num_books for _ in range(num_shelves)]
    queue = []
    level = 0

    # Enqueue the initial state
    queue.append((0, 0, 0, 0))
    visited[0][0] = True

    # Breadth-first search
    while queue:
        # Dequeue the current state
        shelf, book, level, moves = queue.pop(0)

        # If the current state is the final state, return the number of moves
        if shelves[shelf] == visited:
            return moves

        # If the current state is not the final state, enqueue the next states
        for i in range(num_shelves):
            for j in range(num_books):
                if not visited[i][j] and shelves[i][j] == shelves[shelf][book]:
                    queue.append((i, j, level + 1, moves + 1))
                    visited[i][j] = True

    # If the final state is not found, return -1
    return -1

