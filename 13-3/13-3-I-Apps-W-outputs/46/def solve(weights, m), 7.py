
def solve(weights, m):
    # Convert the string of weights to a list of integers
    weights = [int(w) for w in weights]
    # Sort the list of weights in descending order
    weights.sort(reverse=True)
    # Initialize the sum of weights on the left and right scalepans
    left_sum = 0
    right_sum = 0
    # Initialize the list of weights to be placed on the scales
    scales = []
    # Loop through the weights and place them on the scales according to the rules
    for i in range(m):
        # If the current weight is different from the previous weight and the sum of weights on the left scalepan is less than the sum on the right scalepan, place the weight on the left scalepan
        if weights[i] != weights[i-1] and left_sum < right_sum:
            left_sum += weights[i]
            scales.append(weights[i])
        # Otherwise, place the weight on the right scalepan
        else:
            right_sum += weights[i]
            scales.append(weights[i])
    # If the total number of weights placed on the scales is equal to m, return YES and the list of weights
    if len(scales) == m:
        return "YES\n" + " ".join(str(w) for w in scales)
    # Otherwise, return NO
    else:
        return "NO"

