
def solve(numbers):
    # Split the input string into a list of integers
    numbers = [int(num) for num in numbers.split()]
    
    # Initialize the equation string
    equation = ""
    
    # Iterate over the possible operations
    for operation in ["+", "-", "*", "/"]:
        # Iterate over the possible combinations of integers and operations
        for num1 in numbers:
            for num2 in numbers:
                if num1 != num2:
                    # Check if the equation is valid
                    if eval(str(num1) + operation + str(num2)) == numbers[2]:
                        # If the equation is valid, return it
                        equation = str(num1) + operation + str(num2) + "=" + str(numbers[2])
                        return equation
    
    # If no equation is found, return None
    return None

def main():
    numbers = input("Enter three integers separated by spaces: ")
    equation = solve(numbers)
    if equation:
        print(equation)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()

