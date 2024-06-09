
def solve(books):
    # Initialize variables
    presentations = 0
    books_presented = 0

    # Sort the books by title
    books = sorted(books)

    # Loop through the books
    for book in books:
        # If the book has not been presented yet
        if book not in books_presented:
            # Present the book
            books_presented.append(book)
            presentations += 1

    # Return the minimum number of presentations needed
    return presentations

