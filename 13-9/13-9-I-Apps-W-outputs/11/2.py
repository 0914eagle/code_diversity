
def solve(k):
    # Initialize an empty string to store the name
    name = ""
    # Initialize a variable to store the current sum
    current_sum = 0
    # Initialize a variable to store the minimum sum
    min_sum = 1000000
    # Loop through all lowercase letters
    for c in string.ascii_lowercase:
        # Calculate the absolute difference between the current letter and the previous letter
        diff = abs(ord(c) - ord(name[-1])) if name else 0
        # Add the absolute difference to the current sum
        current_sum += diff
        # If the current sum is equal to the target number, return the current name
        if current_sum == k:
            return name
        # If the current sum is less than the target number and the current sum is less than the minimum sum, update the minimum sum and the name
        elif current_sum < k and current_sum < min_sum:
            min_sum = current_sum
            name = c
    # If no name is found, return the empty string
    return ""

