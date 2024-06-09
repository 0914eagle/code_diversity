
def solve_problem(weights, m):
    # Convert the string of weights to a list of integers
    weights = [int(w) for w in weights]
    # Sort the list of weights in descending order
    weights.sort(reverse=True)
    # Initialize the sum of the weights on the left and right scalepans
    left_sum = 0
    right_sum = 0
    # Initialize the list of weights to return
    result = []
    # Iterate through the weights in descending order
    for i, weight in enumerate(weights):
        # If the current weight is not the same as the previous weight
        if i == 0 or weight != weights[i - 1]:
            # Add the current weight to the list of weights to return
            result.append(weight)
            # If the current weight is odd
            if weight % 2 == 1:
                # Add the current weight to the left scalepan
                left_sum += weight
                # If the left scalepan is heavier than the right scalepan
                if left_sum > right_sum:
                    # Add the current weight to the right scalepan
                    right_sum += weight
            # If the current weight is even
            else:
                # Add the current weight to the right scalepan
                right_sum += weight
                # If the right scalepan is heavier than the left scalepan
                if right_sum > left_sum:
                    # Add the current weight to the left scalepan
                    left_sum += weight
        # If the current weight is the same as the previous weight
        else:
            # If the current weight is odd
            if weight % 2 == 1:
                # Add the current weight to the left scalepan
                left_sum += weight
            # If the current weight is even
            else:
                # Add the current weight to the right scalepan
                right_sum += weight
    # If the total number of weights is odd
    if m % 2 == 1:
        # If the left scalepan is heavier than the right scalepan
        if left_sum > right_sum:
            # Add the last weight to the right scalepan
            result.append(weights[0])
        # If the right scalepan is heavier than the left scalepan
        else:
            # Add the last weight to the left scalepan
            result.append(weights[0])
    # If the total number of weights is even
    else:
        # If the left scalepan is heavier than the right scalepan
        if left_sum > right_sum:
            # Add the last two weights to the right scalepan
            result.append(weights[0])
            result.append(weights[1])
        # If the right scalepan is heavier than the left scalepan
        else:
            # Add the last two weights to the left scalepan
            result.append(weights[0])
            result.append(weights[1])
    # Return the list of weights
    return result

