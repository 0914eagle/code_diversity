
def solve(x):
    # Calculate the sum of the numbers on the dice
    sum_of_numbers = sum(range(2, 8))
    
    # Check if the sum of the numbers on the dice is greater than or equal to x
    if sum_of_numbers >= x:
        # If it is, return the number of rolls needed to get x points
        return sum_of_numbers - x + 1
    else:
        # If it's not, return -1
        return -1

