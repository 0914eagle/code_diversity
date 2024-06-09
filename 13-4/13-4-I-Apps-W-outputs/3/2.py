
def solve(n, guard_prices):
    # Initialize variables
    min_cost = 1000000
    chosen_guardpost = -1
    chocolate_cost = -1
    juice_cost = -1

    # Iterate through each guardpost
    for i, guard_price in enumerate(guard_prices, start=1):
        # Calculate the minimum cost to buy gifts for each guardpost
        chocolate_cost = max(guard_price[0], guard_price[2])
        juice_cost = max(guard_price[1], guard_price[3])
        total_cost = chocolate_cost + juice_cost

        # Check if the total cost is less than or equal to the given amount
        if total_cost <= n and total_cost < min_cost:
            min_cost = total_cost
            chosen_guardpost = i

    # Return the chosen guardpost and the costs of the gifts
    return [chosen_guardpost, chocolate_cost, juice_cost]

