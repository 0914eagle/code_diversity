
def get_max_profit(n, a, difficulties, costs):
    # Sort the problems by difficulty in increasing order
    sorted_problems = sorted(range(n), key=lambda i: difficulties[i])

    # Initialize the maximum profit and the current profit
    max_profit = 0
    current_profit = 0

    # Loop through the problems and calculate the profit for each consecutive segment
    for i in range(n):
        # Calculate the profit for the current problem
        current_profit += a - costs[sorted_problems[i]]

        # If the current profit is greater than the maximum profit, update the maximum profit
        if current_profit > max_profit:
            max_profit = current_profit

        # Calculate the gap between the current problem and the next problem
        if i < n - 1:
            gap = (difficulties[sorted_problems[i + 1]] - difficulties[sorted_problems[i]]) ** 2
        else:
            gap = 0

        # If the gap is greater than the current profit, do not include the current problem in the segment
        if gap > current_profit:
            continue

        # If the current profit plus the gap is greater than the maximum profit, update the maximum profit
        if current_profit + gap > max_profit:
            max_profit = current_profit + gap

    return max_profit

