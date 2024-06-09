
def get_maximum_score(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the score and the number of numbers
    score = 0
    num_numbers = len(numbers)
    # Loop through the numbers and perform the tasks
    while num_numbers > 0:
        # If there is only one number left, throw it out
        if num_numbers == 1:
            num_numbers -= 1
        # Otherwise, split the group into two non-empty groups and give them to Toastman
        else:
            # Find the middle index of the numbers
            mid = num_numbers // 2
            # Add the sum of the numbers to the score
            score += sum(numbers[:mid])
            # Give the first group to Toastman
            numbers = numbers[mid:]
            # Update the number of numbers
            num_numbers = len(numbers)
    # Return the maximum possible score
    return score

