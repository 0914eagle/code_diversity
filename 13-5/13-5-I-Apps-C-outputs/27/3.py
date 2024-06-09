
def get_max_score(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the score and the number of numbers
    score = 0
    num_numbers = len(numbers)
    # Loop through the numbers and process them
    while num_numbers > 0:
        # If there is only one number left, throw it out
        if num_numbers == 1:
            num_numbers -= 1
        # If there are more than one number, split them into two non-empty groups
        else:
            # Find the middle index
            mid = num_numbers // 2
            # Add the sum of the numbers to the score
            score += sum(numbers[:mid])
            # Remove the numbers from the list
            numbers = numbers[mid:]
            # Decrement the number of numbers
            num_numbers -= mid
    # Return the score
    return score

