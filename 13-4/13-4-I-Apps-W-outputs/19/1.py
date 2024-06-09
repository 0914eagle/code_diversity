
def solve(n, d, a, m):
    # Calculate the total cost of using all the hooks
    total_cost = sum(a)

    # Calculate the maximum number of guests that can use the hooks without paying a fine
    max_guests = total_cost // d

    # If the number of guests is less than or equal to the maximum number of guests that can use the hooks without paying a fine, then the answer is the total cost
    if m <= max_guests:
        return total_cost

    # Otherwise, calculate the number of guests that can use the hooks without paying a fine and the number of guests that will have to pay a fine
    num_guests_no_fine = max_guests
    num_guests_fine = m - num_guests_no_fine

    # Calculate the total cost of using the hooks without paying a fine
    total_cost_no_fine = num_guests_no_fine * total_cost // m

    # Calculate the total cost of paying the fine
    total_cost_fine = num_guests_fine * d

    # Return the difference between the total cost of using the hooks without paying a fine and the total cost of paying the fine
    return total_cost_no_fine - total_cost_fine

