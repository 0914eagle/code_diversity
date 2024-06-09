
def solve(arr):
    # Calculate the sum of the array
    sum = sum(arr)
    # Calculate the sum of the positive elements
    pos_sum = sum(x for x in arr if x > 0)
    # Calculate the sum of the negative elements
    neg_sum = sum(x for x in arr if x < 0)
    # Return the maximum sum
    return max(sum, pos_sum, neg_sum)

