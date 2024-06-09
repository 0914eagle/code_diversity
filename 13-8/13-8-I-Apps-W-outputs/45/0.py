
def solve_problem(n, k, seats):
    # Initialize the variables
    status_passengers = 0
    regular_passengers = 0
    neighbors = 0
    
    # Loop through each row of seats
    for row in seats:
        # Loop through each seat in the row
        for seat in row:
            # Check if the seat is occupied by a status passenger
            if seat == "S":
                status_passengers += 1
            # Check if the seat is occupied by a regular passenger
            elif seat == "P":
                regular_passengers += 1
    
    # Calculate the total number of neighbors for each status passenger
    for i in range(status_passengers):
        neighbors += status_passengers - i - 1
    
    # Calculate the total number of neighbors for each regular passenger
    for i in range(regular_passengers):
        neighbors += min(i, regular_passengers - i - 1)
    
    # Return the minimum number of neighbors
    return neighbors

