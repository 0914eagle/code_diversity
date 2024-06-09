
def get_max_profit(difficulties, costs, profit):
    # Sort the problems by difficulty in ascending order
    sorted_problems = sorted(enumerate(difficulties), key=lambda x: x[1])

    # Initialize the maximum profit and the current profit
    max_profit = 0
    current_profit = 0

    # Iterate through the sorted problems
    for i in range(len(sorted_problems)):
        # Calculate the current profit by adding the profit of the current problem
        current_profit += profit

        # If the current profit is greater than the maximum profit, update the maximum profit
        if current_profit > max_profit:
            max_profit = current_profit

        # Calculate the gap between the current problem and the next problem
        if i != len(sorted_problems) - 1:
            gap = (sorted_problems[i+1][1] - sorted_problems[i][1]) ** 2
        else:
            gap = 0

        # Subtract the cost of the current problem from the current profit
        current_profit -= costs[sorted_problems[i][0]] + gap

    return max_profit

