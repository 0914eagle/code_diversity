
def get_equation(numbers):
    # Initialize a list to store the possible operations
    operations = ["+", "-", "*", "/"]
    
    # Loop through the possible operations
    for operation in operations:
        # Check if the equation is valid
        if is_valid_equation(numbers, operation):
            # If the equation is valid, return it
            return " ".join(map(str, numbers)) + " " + operation + " " + str(numbers[0])
    
    # If no valid equation is found, return None
    return None

def is_valid_equation(numbers, operation):
    # Check if the operation is addition, subtraction, multiplication, or division
    if operation == "+":
        return numbers[0] + numbers[1] == numbers[2]
    elif operation == "-":
        return numbers[0] - numbers[1] == numbers[2]
    elif operation == "*":
        return numbers[0] * numbers[1] == numbers[2]
    elif operation == "/":
        return numbers[0] / numbers[1] == numbers[2]
    else:
        return False

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(get_equation(numbers))

