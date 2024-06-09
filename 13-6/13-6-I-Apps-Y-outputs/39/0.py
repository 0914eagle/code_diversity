
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Create a list to store the possible equations
    equations = []
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Get the current number
        num1 = numbers[i]
        # Iterate over the remaining numbers
        for j in range(i+1, len(numbers)):
            # Get the current number
            num2 = numbers[j]
            # Iterate over the possible operations
            for op in ["+", "-", "*", "/"]:
                # Check if the current operation is valid
                if op == "/" and num1 % num2 != 0:
                    continue
                # Check if the current equation is valid
                if eval(str(num1) + op + str(num2)) == num1 * num2:
                    # Add the equation to the list
                    equations.append(str(num1) + op + str(num2))
    # Return any of the possible equations
    return equations[0]

def main():
    numbers = input("Enter three numbers separated by spaces: ")
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

