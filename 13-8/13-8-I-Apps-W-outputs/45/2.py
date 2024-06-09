
def solve(n, k, rows):
    # Initialize the number of neighbors for each status passenger to 0
    neighbors = [0] * n

    # Loop through each row of seats
    for i in range(n):
        # If the current seat is empty, continue to the next seat
        if rows[i] == ".":
            continue

        # If the current seat is not empty, check if it is a status passenger
        if rows[i] == "S":
            # If the current seat is a status passenger, increment the number of neighbors
            neighbors[i] += 1

            # If the current seat is not the first seat in the row, check if the previous seat is empty
            if i > 0 and rows[i - 1] == ".":
                # If the previous seat is empty, increment the number of neighbors
                neighbors[i] += 1

            # If the current seat is not the last seat in the row, check if the next seat is empty
            if i < n - 1 and rows[i + 1] == ".":
                # If the next seat is empty, increment the number of neighbors
                neighbors[i] += 1

    # Find the minimum number of neighbors
    min_neighbors = min(neighbors)

    # Initialize the plan for the passenger distribution
    plan = ["."] * n

    # Loop through each seat
    for i in range(n):
        # If the current seat is empty, continue to the next seat
        if rows[i] == ".":
            continue

        # If the current seat is not empty, check if it is a status passenger
        if rows[i] == "S":
            # If the current seat is a status passenger, check if it has the minimum number of neighbors
            if neighbors[i] == min_neighbors:
                # If the current seat has the minimum number of neighbors, mark it as a passenger seat
                plan[i] = "x"

    # Return the plan for the passenger distribution
    return "".join(plan)

