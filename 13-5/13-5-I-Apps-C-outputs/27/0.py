
def get_max_score(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the score and the number of numbers
    score = 0
    num_numbers = len(numbers)
    # Loop through the numbers and calculate the score
    for i in range(num_numbers):
        # If there is only one number left, add it to the score and break the loop
        if i == num_numbers - 1:
            score += numbers[i]
            break
        # If there are more than one number left, split the group in half and add the sum of the two groups to the score
        else:
            score += numbers[i] + numbers[i + 1]
            i += 1
    return score

