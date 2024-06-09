
def get_max_profit(n, a, d, c):
    # Sort the tasks by difficulty
    sorted_tasks = sorted(zip(d, c), key=lambda x: x[0])

    # Initialize the maximum profit and the current profit
    max_profit = 0
    current_profit = 0

    # Iterate through the tasks and calculate the profit for each consecutive segment
    for i in range(n):
        current_profit += a * sorted_tasks[i][0] - sorted_tasks[i][1]
        max_profit = max(max_profit, current_profit)

    return max_profit

