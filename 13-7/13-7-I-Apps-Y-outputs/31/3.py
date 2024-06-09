
def solve(arr):
    # Count the number of positive and negative numbers
    positive = 0
    negative = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
    
    # If the number of positive numbers is greater than the number of negative numbers,
    # then we need to insert negative numbers to make the sum equal
    if positive > negative:
        return positive - negative
    # If the number of negative numbers is greater than the number of positive numbers,
    # then we need to insert positive numbers to make the sum equal
    else:
        return negative - positive

