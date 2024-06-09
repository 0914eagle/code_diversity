
def solve(books):
    # Sort the books by height in descending order
    books.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the variables for the three shelves
    shelf1 = []
    shelf2 = []
    shelf3 = []
    
    # Loop through the books and assign them to the shelves
    for book in books:
        if book[0] > 200:
            shelf1.append(book)
        elif book[0] > 150:
            shelf2.append(book)
        else:
            shelf3.append(book)
    
    # Calculate the area of the bookcase
    area = 0
    for shelf in [shelf1, shelf2, shelf3]:
        area += max([book[1] for book in shelf]) * len(shelf)
    
    return area

