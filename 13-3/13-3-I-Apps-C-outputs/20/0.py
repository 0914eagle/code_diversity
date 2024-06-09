
def get_minimum_presentations(boys, girls, books):
    # Initialize variables
    presentations = 0
    books_presented = 0

    # Sort the books by title
    books = sorted(books)

    # Loop through each book
    for book in books:
        # Check if the book has been presented already
        if book not in books_presented:
            # Increment the number of presentations
            presentations += 1
            # Add the book to the list of presented books
            books_presented.append(book)

    # Return the minimum number of presentations
    return presentations

