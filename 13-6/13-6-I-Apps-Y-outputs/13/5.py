
def reconstruct_equation(numbers):
    # Convert the input string to a list of integers
    numbers = [int(x) for x in numbers.split()]
    
    # Create a list to store the possible operations
    operations = ['+', '-', '*', '/']
    
    # Loop through the possible operations
    for operation in operations:
        # Check if the equation is valid
        if eval(f"{numbers[0]} {operation} {numbers[1]}") == numbers[2]:
            # If the equation is valid, return the equation
            return f"{numbers[0]} {operation} {numbers[1]} = {numbers[2]}"
    
    # If no equation is valid, return None
    return None

