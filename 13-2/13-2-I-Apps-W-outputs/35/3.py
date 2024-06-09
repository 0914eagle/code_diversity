
def get_min_vertical_books(books):
    # Sort the books by width in descending order
    books.sort(key=lambda x: x[1], reverse=True)
    # Initialize the total thickness of the vertical books to 0
    total_thickness = 0
    # Loop through the books and add them to the vertical books if their thickness is 1
    for book in books:
        if book[0] == 1:
            total_thickness += book[0]
    return total_thickness

