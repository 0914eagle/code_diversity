
def solve_problem(weights, m):
    # Convert the string of weights to a list of integers
    weights = [int(w) for w in weights]
    # Sort the list of weights in descending order
    weights.sort(reverse=True)
    # Initialize the sum of weights on each scalepan to 0
    left_sum = 0
    right_sum = 0
    # Initialize the list of weights to return
    result = []
    # Iterate through the weights and put them on the scales
    for i, weight in enumerate(weights):
        # If the current weight is not the same as the previous weight
        if i == 0 or weight != weights[i - 1]:
            # If the current weight is odd
            if weight % 2 == 1:
                # Put the weight on the left scalepan
                left_sum += weight
                result.append(weight)
            # If the current weight is even
            else:
                # Put the weight on the right scalepan
                right_sum += weight
                result.append(weight)
        # If the current weight is the same as the previous weight
        else:
            # If the current weight is odd
            if weight % 2 == 1:
                # Put the weight on the right scalepan
                right_sum += weight
                result.append(weight)
            # If the current weight is even
            else:
                # Put the weight on the left scalepan
                left_sum += weight
                result.append(weight)
        # If the sum of weights on one scalepan is greater than the other scalepan
        if abs(left_sum - right_sum) > 1:
            # Return "NO"
            return "NO"
    # If we have placed all m weights on the scales
    if len(result) == m:
        # Return "YES" and the list of weights
        return "YES\n" + " ".join(map(str, result))
    # If we have not placed all m weights on the scales
    else:
        # Return "NO"
        return "NO"

