
def solve(weights, m):
    # Convert the string of weights to a list of integers
    weights = [int(w) for w in weights]
    # Sort the list of weights in descending order
    weights.sort(reverse=True)
    # Initialize the sum of the weights on the left and right scalepans
    left_sum = 0
    right_sum = 0
    # Initialize the list of weights to return
    result = []
    # Iterate through the weights
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
                # If the left scalepan is heavier than the right scalepan
                if left_sum > right_sum:
                    # Add the current weight to the right scalepan
                    right_sum += weight
            # If the current weight is even
            else:
                # If the right scalepan is heavier than the left scalepan
                if right_sum > left_sum:
                    # Add the current weight to the left scalepan
                    left_sum += weight
    # If the number of weights is odd and the left scalepan is heavier than the right scalepan
    if len(weights) % 2 == 1 and left_sum > right_sum:
        # Add the last weight to the right scalepan
        right_sum += weights[-1]
    # If the number of weights is even and the right scalepan is heavier than the left scalepan
    elif len(weights) % 2 == 0 and right_sum > left_sum:
        # Add the last weight to the left scalepan
        left_sum += weights[-1]
    # If the number of weights is odd and the left scalepan is heavier than the right scalepan
    if len(weights) % 2 == 1 and left_sum > right_sum:
        # Add the last weight to the right scalepan
        right_sum += weights[-1]
    # If the number of weights is even and the right scalepan is heavier than the left scalepan
    elif len(weights) % 2 == 0 and right_sum > left_sum:
        # Add the last weight to the left scalepan
        left_sum += weights[-1]
    # If the number of weights is odd and the left scalepan is heavier than the right scalepan
    if len(weights) % 2 == 1 and left_sum > right_sum:
        # Add the last weight to the right scalepan
        right_sum += weights[-1]
    # If the number of weights is even and the right scalepan is heavier than the left scalepan
    elif len(weights) % 2 == 0 and right_sum > left_sum:
        # Add the last weight to the left scalepan
        left_sum += weights[-1]
    # If the total number of weights is not equal to m
    if len(result) != m:
        return "NO"
    # If the total weight on the left scalepan is not equal to the total weight on the right scalepan
    if left_sum != right_sum:
        return "NO"
    # Return the list of weights
    return "YES\n" + " ".join(str(w) for w in result)

