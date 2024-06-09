
def get_max_profit(n, a, difficulties, costs):
    # Sort the problems by difficulty in increasing order
    sorted_problems = sorted(range(n), key=lambda i: difficulties[i])

    # Initialize the maximum profit and the current profit
    max_profit = 0
    current_profit = 0

    # Iterate through the problems and calculate the profit for each consecutive segment
    for i in range(n):
        current_profit += a * difficulties[sorted_problems[i]]
        current_profit -= costs[sorted_problems[i]]
        max_profit = max(max_profit, current_profit)

    return max_profit

