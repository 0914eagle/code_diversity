
def read_books(desk_a, desk_b, k):
    # Sort the books on both desks by their reading time
    desk_a.sort(key=lambda x: x[1])
    desk_b.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of the books read and the total time spent
    books_read = 0
    total_time = 0
    
    # Loop until we run out of books or reach the time limit
    while books_read < len(desk_a) and total_time < k:
        # Check if the next book on Desk A is faster than the next book on Desk B
        if desk_a[0][1] < desk_b[0][1]:
            # Read the book from Desk A and remove it from the list
            books_read += 1
            total_time += desk_a[0][1]
            desk_a.pop(0)
        else:
            # Read the book from Desk B and remove it from the list
            books_read += 1
            total_time += desk_b[0][1]
            desk_b.pop(0)
    
    # Return the number of books read
    return books_read

