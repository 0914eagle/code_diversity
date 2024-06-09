
def get_max_profit(n, a, difficulties, costs):
    # Sort the problems by difficulty in increasing order
    sorted_problems = sorted(enumerate(difficulties), key=lambda x: x[1])

    # Initialize the maximum profit and the current profit
    max_profit = 0
    current_profit = 0

    # Iterate through the sorted problems
    for i in range(n):
        # Calculate the current profit for the current problem
        current_profit += a - costs[i]

        # If the current profit is greater than the maximum profit, update the maximum profit
        if current_profit > max_profit:
            max_profit = current_profit

        # If the current problem is not the last problem, calculate the gap between the current problem and the next problem
        if i != n - 1:
            gap = (difficulties[i + 1] - difficulties[i]) ** 2
            current_profit -= gap

    return max_profit

