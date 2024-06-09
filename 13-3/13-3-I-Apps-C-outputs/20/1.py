
def get_minimum_presentations(boys, girls, books):
    # Initialize a dictionary to store the books read by each student
    books_read = {}

    # Add the books read by each boy to the dictionary
    for boy in boys:
        books_read[boy] = set(books[boy])

    # Add the books read by each girl to the dictionary
    for girl in girls:
        books_read[girl] = set(books[girl])

    # Initialize a set to store the books that have been presented
    presented_books = set()

    # Initialize a counter for the number of presentations
    presentations = 0

    # Loop through each student and their books
    for student in boys + girls:
        # Check if the student has any books to present
        if len(books_read[student]) > 0:
            # Add the presented books to the presented_books set
            presented_books |= books_read[student]

            # Increment the number of presentations
            presentations += 1

    # Return the minimum number of presentations needed
    return presentations

