
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Get the unique elements of the list
    unique_numbers = set(numbers)
    # Check if there are three unique numbers
    if len(unique_numbers) == 3:
        # Get the first two numbers
        num1, num2 = numbers
        # Get the third number
        num3 = numbers[2]
        # Check if the first two numbers add up to the third number
        if num1 + num2 == num3:
            return f"{num1}+{num2}={num3}"
        # Check if the first two numbers multiply to the third number
        if num1 * num2 == num3:
            return f"{num1}*{num2}={num3}"
        # Check if the first number subtracted from the second number equals the third number
        if num1 - num2 == num3:
            return f"{num1}-{num2}={num3}"
        # Check if the first number divided by the second number equals the third number
        if num1 / num2 == num3:
            return f"{num1}/{num2}={num3}"
    # If no equation can be found, return "NO EQUATION"
    return "NO EQUATION"

def main():
    # Get the input numbers from the user
    numbers = input("Enter three numbers: ")
    # Call the get_equation function and pass in the numbers
    equation = get_equation(numbers)
    # Print the equation
    print(equation)

if __name__ == '__main__':
    main()

