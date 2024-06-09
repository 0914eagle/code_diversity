
def reconstruct_equation(numbers):
    # Split the input string into a list of integers
    numbers = [int(num) for num in numbers.split()]
    # Initialize the equation with the first two numbers
    equation = str(numbers[0]) + " " + str(numbers[1]) + " "
    # Check which operation to use based on the third number
    if numbers[2] % numbers[0] == 0:
        # Division
        equation += "÷ " + str(numbers[2] // numbers[0])
    elif numbers[2] % numbers[1] == 0:
        # Division
        equation += "÷ " + str(numbers[2] // numbers[1])
    elif numbers[0] + numbers[1] == numbers[2]:
        # Addition
        equation += "+" + str(numbers[2] - numbers[0])
    elif numbers[0] - numbers[1] == numbers[2]:
        # Subtraction
        equation += "-" + str(numbers[2] - numbers[0])
    elif numbers[0] * numbers[1] == numbers[2]:
        # Multiplication
        equation += "× " + str(numbers[2] // numbers[0])
    else:
        # Multiplication
        equation += "× " + str(numbers[2] // numbers[1])
    return equation

