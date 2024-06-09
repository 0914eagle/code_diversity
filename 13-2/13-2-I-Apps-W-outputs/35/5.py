
def get_min_vertical_books(books):
    # Sort the books by width in descending order
    books.sort(key=lambda x: x[1], reverse=True)
    # Initialize the minimum total thickness to 0
    min_thickness = 0
    # Loop through the books and add them to the vertical books
    for book in books:
        # If the total thickness of the vertical books is less than the width of the current book, add the current book to the vertical books
        if min_thickness < book[1]:
            min_thickness += book[0]
        # Otherwise, add the current book to the horizontal books
        else:
            min_thickness = max(min_thickness, book[0])
    return min_thickness

