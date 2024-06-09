
def get_min_area(books):
    # Sort the books by height in descending order
    books = sorted(books, key=lambda x: x[0], reverse=True)
    
    # Initialize the areas of the three shelves
    shelf_1_area = 0
    shelf_2_area = 0
    shelf_3_area = 0
    
    # Loop through the books and assign them to the shelves
    for book in books:
        # Check if the book fits on shelf 1
        if book[1] <= shelf_1_area:
            shelf_1_area += book[1]
        # Check if the book fits on shelf 2
        elif book[1] <= shelf_2_area:
            shelf_2_area += book[1]
        # Check if the book fits on shelf 3
        elif book[1] <= shelf_3_area:
            shelf_3_area += book[1]
        # If the book doesn't fit on any shelf, return -1
        else:
            return -1
    
    # Return the minimum area
    return min(shelf_1_area * shelf_2_area, shelf_2_area * shelf_3_area, shelf_3_area * shelf_1_area)

