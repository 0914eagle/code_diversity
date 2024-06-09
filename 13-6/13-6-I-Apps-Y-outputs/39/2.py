
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Get the unique numbers
    unique_numbers = set(numbers)
    # Get the operation
    operation = get_operation(numbers)
    # Return the equation
    return f"{unique_numbers[0]} {operation} {unique_numbers[1]}={unique_numbers[2]}"

def get_operation(numbers):
    # Check if the numbers can be added
    if numbers[0] + numbers[1] == numbers[2]:
        return "+"
    # Check if the numbers can be subtracted
    elif numbers[0] - numbers[1] == numbers[2]:
        return "-"
    # Check if the numbers can be multiplied
    elif numbers[0] * numbers[1] == numbers[2]:
        return "*"
    # Check if the numbers can be divided
    elif numbers[0] / numbers[1] == numbers[2]:
        return "/"
    # If no operation can be found, return None
    else:
        return None

if __name__ == '__main__':
    numbers = input("Enter three integers separated by spaces: ")
    print(get_equation(numbers))

