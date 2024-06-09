
def solve(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the guessed numbers
    a = b = c = 0
    # Iterate over the numbers
    for i in range(len(numbers)):
        # If the current number is equal to the sum of the previous two numbers, then it is one of the guessed numbers
        if numbers[i] == numbers[i-2] + numbers[i-1]:
            a = numbers[i-2]
            b = numbers[i-1]
            c = numbers[i]
            break
    # Return the guessed numbers in any order
    return [a, b, c]

