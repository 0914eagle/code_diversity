
def get_guardpost(n, guard_prices):
    # Initialize variables
    guardpost = -1
    chocolate_cost = -1
    juice_cost = -1

    # Iterate through the guardposts
    for i, prices in enumerate(guard_prices, start=1):
        # Get the minimum chocolate and juice prices for the current guardpost
        min_chocolate_price, min_juice_price = prices

        # Calculate the cost of the chocolate and juice for the current guardpost
        chocolate_cost = min_chocolate_price
        juice_cost = min_juice_price

        # Check if the cost is less than or equal to the given amount
        if chocolate_cost + juice_cost <= n:
            # If it is, break the loop and return the guardpost, chocolate cost, and juice cost
            guardpost = i
            break

    # Return the guardpost, chocolate cost, and juice cost
    return guardpost, chocolate_cost, juice_cost

