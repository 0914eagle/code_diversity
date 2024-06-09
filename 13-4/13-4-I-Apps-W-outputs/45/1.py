
def get_max_sweets(n, s, sugar_costs):
    # Sort the sugar costs in non-decreasing order of cost
    sugar_costs.sort(key=lambda x: x[0])

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the sugar costs and try to buy each type of sugar
    for i in range(n):
        # Calculate the cost of the current sugar in dollars and cents
        cost_dollars = sugar_costs[i][0]
        cost_cents = sugar_costs[i][1]

        # Check if the current sugar is within Caisa's budget
        if cost_dollars <= s:
            # Calculate the number of sweets that Caisa will get as change
            sweets = s * 100 - cost_dollars * 100 + cost_cents

            # Update the maximum number of sweets if necessary
            max_sweets = max(max_sweets, sweets)

            # Remove the current sugar from the budget
            s -= cost_dollars

    # Return the maximum number of sweets that Caisa can get
    return max_sweets

