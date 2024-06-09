
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    visited = [[False for _ in range(num_books)] for _ in range(num_shelves)]
    queue = [(0, 0, 0)]
    level = 0

    # BFS to find the minimum number of lifting
    while queue:
        shelf, book, level = queue.pop(0)
        if visited[shelf][book]:
            continue
        visited[shelf][book] = True

        # Check if the current state matches the wanted state
        if shelves[shelf][book] == 0:
            continue
        if shelf == num_shelves - 1 and book == num_books - 1:
            return level

        # Enqueue the neighboring states
        for i in range(num_shelves):
            for j in range(num_books):
                if shelves[i][j] == shelves[shelf][book] and not visited[i][j]:
                    queue.append((i, j, level + 1))

    # If no matching state is found, return -1
    return -1

