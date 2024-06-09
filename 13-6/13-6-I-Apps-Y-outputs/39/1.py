
def reconstruct_equation(numbers):
    # Split the input string into a list of integers
    numbers = [int(x) for x in numbers.split()]
    
    # Create a list of all possible operations
    operations = ['+', '-', '*', '/']
    
    # Loop through all possible operations
    for operation in operations:
        # Check if the equation is valid
        if is_valid_equation(numbers, operation):
            # If the equation is valid, return it
            return f"{numbers[0]} {operation} {numbers[1]} = {numbers[2]}"
    
    # If no valid equation is found, return None
    return None

def is_valid_equation(numbers, operation):
    # Check if the equation is valid
    if operation == '+':
        return numbers[0] + numbers[1] == numbers[2]
    elif operation == '-':
        return numbers[0] - numbers[1] == numbers[2]
    elif operation == '*':
        return numbers[0] * numbers[1] == numbers[2]
    else:
        return numbers[0] / numbers[1] == numbers[2]

if __name__ == '__main__':
    numbers = input("Enter three integers separated by spaces: ")
    equation = reconstruct_equation(numbers)
    if equation:
        print(equation)
    else:
        print("No valid equation found.")

