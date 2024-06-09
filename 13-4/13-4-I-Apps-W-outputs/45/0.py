
def get_max_sweets(n, s, sugar_costs):
    # Sort the sugar costs in non-decreasing order of cost
    sugar_costs.sort(key=lambda x: x[0])

    # Initialize the maximum number of sweets as 0
    max_sweets = 0

    # Iterate through the sugar costs and calculate the maximum number of sweets that can be bought
    for i in range(n):
        cost = sugar_costs[i][0]
        cents = sugar_costs[i][1]
        if s >= cost:
            max_sweets += cents
            s -= cost
        else:
            break

    # Return the maximum number of sweets that can be bought
    return max_sweets

