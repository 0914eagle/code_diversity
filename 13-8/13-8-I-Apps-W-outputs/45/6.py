
def solve_problem(n, k, rows):
    # Initialize the number of neighbors for each status passenger to 0
    neighbors = [0] * n

    # Loop through each row of seats
    for i in range(n):
        # If the current seat is occupied by a status passenger, skip it
        if rows[i][0] == "S":
            continue

        # If the current seat is occupied by an ordinary passenger, check if it is a neighbor for any status passenger
        if rows[i][0] == "P":
            # Loop through each status passenger in the current row
            for j in range(n):
                # If the current seat is occupied by a status passenger and it is not the current seat, increment the neighbor count
                if rows[i][j] == "S" and j != i:
                    neighbors[j] += 1

    # Sort the neighbors in descending order
    neighbors.sort(reverse=True)

    # Initialize the total number of neighbors to 0
    total_neighbors = 0

    # Loop through each status passenger and add their neighbor count to the total
    for i in range(n):
        total_neighbors += neighbors[i]

    # Return the total number of neighbors
    return total_neighbors

