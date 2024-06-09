
def solve(n, k, seq, costs):
    # Initialize a dictionary to store the minimum effort required to make the sequence unbalanced
    dp = {i: 0 for i in range(n)}

    # Loop through each position in the sequence
    for i in range(n):
        # If the position is already unbalanced, skip it
        if seq[i] != '(' and seq[i] != ')':
            continue

        # If the position is balanced and the cost is negative, update the minimum effort required to make the sequence unbalanced
        if seq[i] == '(' and costs[i] < 0:
            dp[i] = costs[i]

        # If the position is balanced and the cost is positive, update the minimum effort required to make the sequence unbalanced
        if seq[i] == ')' and costs[i] > 0:
            dp[i] = costs[i]

        # If the position is balanced and the cost is zero, skip it
        if seq[i] == '(' and costs[i] == 0:
            continue
        if seq[i] == ')' and costs[i] == 0:
            continue

        # If the position is balanced and the cost is negative, update the minimum effort required to make the sequence unbalanced
        if seq[i] == '(' and costs[i] < 0:
            dp[i] = costs[i]

        # If the position is balanced and the cost is positive, update the minimum effort required to make the sequence unbalanced
        if seq[i] == ')' and costs[i] > 0:
            dp[i] = costs[i]

    # Initialize a variable to store the minimum sum of effort required to make the sequence unbalanced
    min_effort = 0

    # Loop through each position in the sequence
    for i in range(n):
        # If the position is already unbalanced, skip it
        if seq[i] != '(' and seq[i] != ')':
            continue

        # If the position is balanced and the cost is negative, update the minimum sum of effort required to make the sequence unbalanced
        if seq[i] == '(' and costs[i] < 0:
            min_effort += costs[i]

        # If the position is balanced and the cost is positive, update the minimum sum of effort required to make the sequence unbalanced
        if seq[i] == ')' and costs[i] > 0:
            min_effort += costs[i]

        # If the position is balanced and the cost is zero, skip it
        if seq[i] == '(' and costs[i] == 0:
            continue
        if seq[i] == ')' and costs[i] == 0:
            continue

        # If the position is balanced and the cost is negative, update the minimum sum of effort required to make the sequence unbalanced
        if seq[i] == '(' and costs[i] < 0:
            min_effort += costs[i]

        # If the position is balanced and the cost is positive, update the minimum sum of effort required to make the sequence unbalanced
        if seq[i] == ')' and costs[i] > 0:
            min_effort += costs[i]

    # Return the minimum sum of effort required to make the sequence unbalanced
    return min_effort

