
def reconstruct_equation(numbers):
    # Split the input strings into a list of integers
    numbers = [int(n) for n in numbers.split()]
    
    # Create a list of all possible operations
    operations = ['+', '-', '*', '/']
    
    # Iterate over the possible operations
    for operation in operations:
        # Check if the equation is valid
        if eval(f"{numbers[0]} {operation} {numbers[1]}") == numbers[2]:
            # If the equation is valid, return it
            return f"{numbers[0]} {operation} {numbers[1]} = {numbers[2]}"
    
    # If no equation is valid, return None
    return None

