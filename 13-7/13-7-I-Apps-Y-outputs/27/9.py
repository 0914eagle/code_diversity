
def reconstruct_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Initialize the equation with the first two numbers
    equation = str(numbers[0]) + "+" + str(numbers[1])
    # Check if the third number is a valid solution for the equation
    if (numbers[0] + numbers[1]) == numbers[2]:
        return equation + "=" + str(numbers[2])
    # Check if the third number is a valid solution for the equation
    elif (numbers[0] - numbers[1]) == numbers[2]:
        return equation + "=" + str(numbers[2])
    # Check if the third number is a valid solution for the equation
    elif (numbers[0] * numbers[1]) == numbers[2]:
        return equation + "=" + str(numbers[2])
    # Check if the third number is a valid solution for the equation
    elif (numbers[0] / numbers[1]) == numbers[2]:
        return equation + "=" + str(numbers[2])
    # If no solution is found, return None
    else:
        return None

def main():
    numbers = input("Enter three integers separated by spaces: ")
    equation = reconstruct_equation(numbers)
    if equation:
        print(equation)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()

