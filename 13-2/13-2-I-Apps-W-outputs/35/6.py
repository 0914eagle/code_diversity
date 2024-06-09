
def get_min_thickness(books):
    # Sort the books by width in descending order
    books.sort(key=lambda x: x[1], reverse=True)
    # Initialize the total thickness and width of the vertical books
    total_thickness = 0
    total_width = 0
    # Loop through the books
    for book in books:
        # If the width of the book is greater than the total width of the vertical books,
        # add the book to the vertical books
        if book[1] > total_width:
            total_thickness += book[0]
            total_width += book[1]
        # Otherwise, add the book to the horizontal books
        else:
            total_thickness += book[0]
    return total_thickness

