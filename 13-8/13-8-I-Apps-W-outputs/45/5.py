
def solve(n, k, rows):
    # Initialize variables
    total_seats = 0
    status_seats = 0
    regular_seats = 0
    adjacent_status_seats = 0

    # Iterate through the rows
    for row in rows:
        # Check if the row is empty
        if row == "":
            continue

        # Split the row into individual seats
        seats = row.split("-")

        # Iterate through the seats
        for seat in seats:
            # Check if the seat is empty
            if seat == ".":
                continue

            # Increment the total number of seats
            total_seats += 1

            # Check if the seat is a status seat
            if seat == "S":
                # Increment the number of status seats
                status_seats += 1

                # Check if the seat has an adjacent status seat
                if adjacent_status_seats > 0:
                    # Increment the number of adjacent status seats
                    adjacent_status_seats += 1
                else:
                    # Reset the number of adjacent status seats
                    adjacent_status_seats = 0
            else:
                # Increment the number of regular seats
                regular_seats += 1

    # Calculate the minimum number of adjacent status seats
    min_adjacent_status_seats = min(status_seats, regular_seats)

    # Return the result
    return min_adjacent_status_seats

