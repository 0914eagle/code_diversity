
def get_max_sweets(n, s, sugar_costs):
    # Sort the sugar costs in descending order
    sugar_costs.sort(key=lambda x: x[0], reverse=True)

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the sugar costs
    for sugar_cost in sugar_costs:
        # Calculate the total cost of the sugar
        total_cost = sugar_cost[0] * 100 + sugar_cost[1]

        # Check if the total cost is less than or equal to the amount of money Caisa has
        if total_cost <= s:
            # Calculate the number of sweets that Caisa will get as change
            sweets = s - total_cost

            # Update the maximum number of sweets if necessary
            if sweets > max_sweets:
                max_sweets = sweets

            # Break the loop since we have found the best sugar type
            break

    # Return the maximum number of sweets
    return max_sweets

