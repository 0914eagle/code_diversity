
def solve_problem(n, k, seats):
    # Initialize variables
    status_passengers = 0
    ordinary_passengers = 0
    adjacent_status_passengers = 0

    # Iterate through each row of seats
    for row in seats:
        # Initialize variables for the current row
        current_row_status_passengers = 0
        current_row_ordinary_passengers = 0
        current_row_adjacent_status_passengers = 0

        # Iterate through each seat in the current row
        for seat in row:
            # Check if the current seat is occupied by a status passenger
            if seat == "S":
                current_row_status_passengers += 1
            # Check if the current seat is occupied by an ordinary passenger
            elif seat == "P":
                current_row_ordinary_passengers += 1

        # Update the total number of status passengers and ordinary passengers
        status_passengers += current_row_status_passengers
        ordinary_passengers += current_row_ordinary_passengers

        # Update the total number of adjacent status passengers
        current_row_adjacent_status_passengers = current_row_status_passengers - 1
        adjacent_status_passengers += current_row_adjacent_status_passengers

    # Calculate the minimum number of adjacent status passengers
    min_adjacent_status_passengers = adjacent_status_passengers

    # Return the minimum number of adjacent status passengers and the optimal seating plan
    return min_adjacent_status_passengers, seats

