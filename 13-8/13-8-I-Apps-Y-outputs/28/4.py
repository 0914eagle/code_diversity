
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Initialize the equation variables
    eq_num1 = 0
    eq_num2 = 0
    eq_op = ""
    # Iterate through the possible combinations of numbers and operations
    for num1 in numbers:
        for num2 in numbers:
            if num1 != num2:
                for op in ["+", "-", "*", "/"]:
                    # Calculate the result of the equation
                    result = eval(str(num1) + op + str(num2))
                    # Check if the result is equal to the third number
                    if result == numbers[2]:
                        # If the result is equal, store the numbers and operation in the equation variables
                        eq_num1 = num1
                        eq_num2 = num2
                        eq_op = op
                        break
    # Return the reconstructed equation
    return str(eq_num1) + eq_op + str(eq_num2) + "=" + str(numbers[2])

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

