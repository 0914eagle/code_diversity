
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
            # Increment the number of presentations
            presentations += 1
            # Add the book to the list of presented books
            books_presented.append(book)

    # Return the minimum number of presentations needed
    return presentations

