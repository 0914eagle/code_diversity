
def solve_problem(n, k, rows):
    # Initialize variables
    num_seats = n * 7
    num_status_seats = 0
    num_normal_seats = 0
    num_neighbors = 0
    status_seats = []
    normal_seats = []

    # Count the number of status and normal seats
    for row in rows:
        for seat in row:
            if seat == "S":
                num_status_seats += 1
                status_seats.append(seat)
            elif seat == "P":
                num_normal_seats += 1
                normal_seats.append(seat)

    # Calculate the minimum number of neighbors
    for i in range(num_status_seats):
        num_neighbors += min(num_status_seats - i, i)

    # Add the number of neighbors for the normal seats
    for seat in normal_seats:
        num_neighbors += 1

    # Return the result
    return num_neighbors

