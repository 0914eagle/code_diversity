
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    visited = [[False] * num_books for _ in range(num_shelves)]
    queue = [(0, 0, 0)]
    level = 0

    # Breadth-first search to find the minimum number of lifts
    while queue:
        shelf, book, level = queue.pop(0)
        if visited[shelf][book]:
            continue
        visited[shelf][book] = True

        # Check if the current state is the wanted state
        if shelves[shelf][book] != 0:
            queue.append((shelf, book, level + 1))

        # Move the book to the left or right if possible
        for direction in [-1, 1]:
            new_shelf = shelf + direction
            new_book = book + direction
            if 0 <= new_shelf < num_shelves and 0 <= new_book < num_books:
                queue.append((new_shelf, new_book, level + 1))

        # Take the book and place it on any available shelf
        for new_shelf in range(num_shelves):
            for new_book in range(num_books):
                if shelves[new_shelf][new_book] == 0 and not visited[new_shelf][new_book]:
                    queue.append((new_shelf, new_book, level + 1))

    return level

