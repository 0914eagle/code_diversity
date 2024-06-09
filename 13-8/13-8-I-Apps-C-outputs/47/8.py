
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    visited = [[False for _ in range(num_books)] for _ in range(num_shelves)]
    queue = []
    lifting = 0

    # Enqueue the initial state
    queue.append((0, 0, 0))
    visited[0][0] = True

    # Breadth-first search
    while queue:
        shelf, book, level = queue.pop(0)

        # If we have reached the final state, return the lifting count
        if shelves[shelf] == visited:
            return lifting

        # If we can move the book to the left, enqueue the new state
        if book > 0 and not visited[shelf][book - 1]:
            queue.append((shelf, book - 1, level + 1))
            visited[shelf][book - 1] = True

        # If we can move the book to the right, enqueue the new state
        if book < num_books - 1 and not visited[shelf][book + 1]:
            queue.append((shelf, book + 1, level + 1))
            visited[shelf][book + 1] = True

        # If we can take the book and place it on another shelf, enqueue the new state
        for i in range(num_shelves):
            if not visited[i][book]:
                queue.append((i, book, level + 1))
                visited[i][book] = True

        # Increment the lifting count
        lifting += 1

    # If we reached the end of the search without finding the final state, return -1
    return -1

