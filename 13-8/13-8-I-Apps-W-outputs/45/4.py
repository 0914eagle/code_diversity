
def solve_passenger_problem(row_count, column_count, row_data, passenger_count):
    # Initialize variables
    total_neighbors = 0
    seat_assignments = ["."] * row_count * column_count
    status_passengers = []
    regular_passengers = []

    # Parse the input data
    for i in range(row_count):
        for j in range(column_count):
            if row_data[i][j] == "S":
                status_passengers.append((i, j))
            elif row_data[i][j] == "P":
                regular_passengers.append((i, j))

    # Assign regular passengers to seats
    for passenger in regular_passengers:
        row, col = passenger
        for i in range(row_count):
            for j in range(column_count):
                if seat_assignments[i * column_count + j] == ".":
                    seat_assignments[i * column_count + j] = "P"
                    break

    # Calculate the total number of neighbors for each status passenger
    for passenger in status_passengers:
        row, col = passenger
        neighbor_count = 0
        for i in range(row_count):
            for j in range(column_count):
                if seat_assignments[i * column_count + j] == "P" and (i, j) != passenger:
                    neighbor_count += 1
        total_neighbors += neighbor_count

    return total_neighbors

