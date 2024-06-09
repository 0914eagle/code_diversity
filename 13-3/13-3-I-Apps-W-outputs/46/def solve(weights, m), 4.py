
def solve(weights, m):
    # Convert the string of weights to a list of integers
    weights = [int(w) for w in weights]
    # Sort the list of weights in descending order
    weights.sort(reverse=True)
    # Initialize the sum of the weights on each scalepan to 0
    left_sum = 0
    right_sum = 0
    # Initialize the list of weights to return
    result = []
    # Iterate through the weights in descending order
    for weight in weights:
        # If the current weight is not the same as the previous weight
        if weight != result[-1] if result else True:
            # Add the current weight to the list of weights to return
            result.append(weight)
            # Update the sum of the weights on each scalepan
            left_sum += weight
            right_sum += weight
            # If the sum of the weights on the left scalepan is greater than the sum of the weights on the right scalepan
            if left_sum > right_sum:
                # Swap the sums of the weights on the two scalepans
                left_sum, right_sum = right_sum, left_sum
            # If the number of weights placed on the scales is equal to m
            if len(result) == m:
                # Return the list of weights
                return result
    # If the number of weights placed on the scales is not equal to m
    return "NO"

