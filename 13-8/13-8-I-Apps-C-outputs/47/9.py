
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    visited = [[False for _ in range(num_books)] for _ in range(num_shelves)]
    queue = []
    count = 0

    # Loop through each shelf and book
    for shelf in range(num_shelves):
        for book in range(num_books):
            # If the book is not in its desired position, add it to the queue
            if shelves[shelf][book] != 0 and shelves[shelf][book] != shelf * num_books + book + 1:
                queue.append((shelf, book))
                visited[shelf][book] = True
                count += 1

    # Breadth-first search to move books to their desired positions
    while queue:
        shelf, book = queue.pop(0)
        # If the book is not in its desired position, move it to the left or right
        if shelves[shelf][book] != 0 and shelves[shelf][book] != shelf * num_books + book + 1:
            # Move the book to the left
            if shelf > 0 and not visited[shelf - 1][book]:
                visited[shelf - 1][book] = True
                queue.append((shelf - 1, book))
                count += 1
            # Move the book to the right
            if shelf < num_shelves - 1 and not visited[shelf + 1][book]:
                visited[shelf + 1][book] = True
                queue.append((shelf + 1, book))
                count += 1
            # Move the book to a different shelf
            for i in range(num_shelves):
                if not visited[i][book] and shelves[i][book] == 0:
                    visited[i][book] = True
                    queue.append((i, book))
                    count += 1
                    break

    # If all books are in their desired positions, return the number of lifts required
    if all(all(visited[i][j] for j in range(num_books)) for i in range(num_shelves)):
        return count

    # If it is not possible to arrange the books in the desired way, return -1
    return -1

