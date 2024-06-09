
def solve(shelves):
    # Initialize variables
    num_shelves, num_books = len(shelves), len(shelves[0])
    lifting = 0

    # Loop through each shelf
    for shelf in range(num_shelves):
        # Loop through each book on the shelf
        for book in range(num_books):
            # Check if the book is in its correct place
            if shelves[shelf][book] != book + 1:
                # Find the correct place for the book
                correct_place = shelves[shelf].index(book + 1)

                # Swap the book with the correct place
                shelves[shelf][book], shelves[shelf][correct_place] = shelves[shelf][correct_place], shelves[shelf][book]

                # Increment the number of lifting
                lifting += 1

    # Return the minimal number of lifting
    return lifting

