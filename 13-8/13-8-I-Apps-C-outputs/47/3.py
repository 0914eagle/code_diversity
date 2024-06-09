
def solve(N, M, initial_state, final_state):
    # Initialize the number of lifts to 0
    lifts = 0
    # Initialize a list to store the current state of the shelves
    current_state = [row[:] for row in initial_state]
    # Loop through each shelf
    for shelf in range(N):
        # Loop through each book on the current shelf
        for book in range(M):
            # Check if the current book is in its correct place
            if current_state[shelf][book] != final_state[shelf][book]:
                # If not, check if the book can be moved to its correct place
                if can_move_book(current_state, shelf, book, final_state[shelf][book]):
                    # If it can be moved, move the book and increment the number of lifts
                    move_book(current_state, shelf, book, final_state[shelf][book])
                    lifts += 1
                else:
                    # If it can't be moved, return -1 because it is impossible to arrange the books
                    return -1
    # If all books are in their correct place, return the number of lifts
    return lifts

# Check if a book can be moved to a certain place
def can_move_book(current_state, shelf, book, target):
    # Check if the target place is empty
    if current_state[shelf][target] == 0:
        # If it is empty, check if the book can be moved one place to the left or right
        if (shelf > 0 and current_state[shelf - 1][book] == 0) or (shelf < len(current_state) - 1 and current_state[shelf + 1][book] == 0):
            return True
    return False

# Move a book to a certain place
def move_book(current_state, shelf, book, target):
    # Set the current place of the book to 0
    current_state[shelf][book] = 0
    # Set the target place of the book to its value
    current_state[shelf][target] = book

