
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Create a list to store the possible equations
    equations = []
    # Iterate over the possible operations
    for operation in ["+", "-", "*", "/"]:
        # Iterate over the possible combinations of numbers and operations
        for num1 in numbers:
            for num2 in numbers:
                # Check if the equation is valid
                if num1 + num2 == numbers[2] and operation == "+":
                    equations.append(f"{num1} + {num2} = {numbers[2]}")
                elif num1 - num2 == numbers[2] and operation == "-":
                    equations.append(f"{num1} - {num2} = {numbers[2]}")
                elif num1 * num2 == numbers[2] and operation == "*":
                    equations.append(f"{num1} * {num2} = {numbers[2]}")
                elif num1 / num2 == numbers[2] and operation == "/":
                    equations.append(f"{num1} / {num2} = {numbers[2]}")
    # Return any of the possible equations
    return equations[0]

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

