
def solve(x1, x2, x3, x4):
    # Find the sum of all three numbers
    sum_of_three = x1 + x2 + x3

    # Find the difference between the sum of two numbers and the third number
    diff = x1 + x2 - x3

    # Find the sum of two numbers that add up to the third number
    sum_of_two = (sum_of_three - diff) // 2

    # Find the third number by subtracting the sum of two numbers from the sum of three numbers
    third_number = sum_of_three - sum_of_two

    # Return the guessed numbers in any order
    return sorted([diff, sum_of_two, third_number])

