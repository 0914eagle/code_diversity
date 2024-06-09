
def solve(n, x, vouchers):
    # Sort the vouchers by their cost in non-decreasing order
    vouchers.sort(key=lambda x: x[2])

    # Initialize the minimum cost to infinity
    min_cost = float('inf')

    # Iterate over all possible pairs of vouchers
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Check if the vouchers are disjoint
            if vouchers[i][1] < vouchers[j][0] or vouchers[j][1] < vouchers[i][0]:
                # Calculate the total duration and cost of the vouchers
                total_duration = vouchers[i][1] - vouchers[i][0] + 1 + vouchers[j][1] - vouchers[j][0] + 1
                total_cost = vouchers[i][2] + vouchers[j][2]

                # Check if the total duration is equal to x and the total cost is less than the minimum cost
                if total_duration == x and total_cost < min_cost:
                    # Update the minimum cost
                    min_cost = total_cost

    # Check if a pair of vouchers with the total duration equal to x and minimum cost exists
    if min_cost == float('inf'):
        return -1

    # Return the minimum cost
    return min_cost

