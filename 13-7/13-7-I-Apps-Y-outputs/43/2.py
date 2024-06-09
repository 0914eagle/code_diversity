
def solve(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the guessed numbers
    a, b, c = 0, 0, 0
    # Iterate through the numbers
    for i in range(len(numbers)):
        # Check if the current number is equal to the sum of the previous two numbers
        if numbers[i] == numbers[i-2] + numbers[i-1]:
            # If it is, set the current number as c
            c = numbers[i]
            # Set the previous two numbers as a and b
            a, b = numbers[i-2], numbers[i-1]
            # Break out of the loop
            break
    # Return the guessed numbers in any order
    return a, b, c

