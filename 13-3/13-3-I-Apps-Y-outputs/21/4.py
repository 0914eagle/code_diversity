
def solve():
    N = int(input())
    values = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    # Initialize the maximum possible value of X-Y
    max_value = 0

    # Iterate over all possible combinations of gems
    for i in range(1 << N):
        # Initialize the sum of values and costs for the current combination
        current_value = 0
        current_cost = 0

        # Iterate over the gems in the current combination
        for j in range(N):
            # If the j-th gem is chosen, add its value and cost to the current sum
            if i & (1 << j):
                current_value += values[j]
                current_cost += costs[j]

        # Update the maximum possible value of X-Y if the current combination is better
        max_value = max(max_value, current_value - current_cost)

    return max_value

