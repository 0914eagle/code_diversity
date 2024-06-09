
def solve(shelves):
    # Initialize variables
    n_shelves = len(shelves)
    n_books = len(shelves[0])
    lifting = 0

    # Loop through each shelf
    for shelf in range(n_shelves):
        # Loop through each book on the shelf
        for book in range(n_books):
            # Check if the book is in its correct place
            if shelves[shelf][book] != (shelf * n_books) + book + 1:
                # Check if the book can be moved to its correct place
                if shelves[shelf][book] != 0 and shelves[shelf][book-1] == 0:
                    # Move the book to the left
                    shelves[shelf][book-1] = shelves[shelf][book]
                    shelves[shelf][book] = 0
                    lifting += 1
                elif shelves[shelf][book] != 0 and shelves[shelf][book+1] == 0:
                    # Move the book to the right
                    shelves[shelf][book+1] = shelves[shelf][book]
                    shelves[shelf][book] = 0
                    lifting += 1
                else:
                    # The book cannot be moved, return -1
                    return -1

    # If all books are in their correct place, return the number of lifting
    return lifting

