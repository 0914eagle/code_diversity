
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    visited = [[False for _ in range(num_books)] for _ in range(num_shelves)]
    queue = [(0, 0, 0)]
    count = 0

    # Breadth-first search
    while queue:
        shelf, book, level = queue.pop(0)
        if visited[shelf][book]:
            continue
        visited[shelf][book] = True

        # Check if the book is in the correct position
        if shelves[shelf][book] != 0 and shelves[shelf][book] != level + 1:
            return -1

        # Enqueue the neighbors
        for i in range(shelf - 1, shelf + 2):
            for j in range(book - 1, book + 2):
                if 0 <= i < num_shelves and 0 <= j < num_books and not visited[i][j]:
                    queue.append((i, j, level + 1))

        count += 1

    return count

