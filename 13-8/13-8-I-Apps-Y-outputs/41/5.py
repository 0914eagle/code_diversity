
def reconstruct_equation(numbers):
    # Convert the input string to a list of integers
    numbers = [int(x) for x in numbers.split()]
    
    # Create a list of all possible operations
    operations = ['+', '-', '*', '/']
    
    # Loop through each operation and check if it produces the correct result
    for operation in operations:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    result = eval(str(numbers[i]) + operation + str(numbers[j]))
                    if result == numbers[2]:
                        return str(numbers[i]) + operation + str(numbers[j]) + '=' + str(numbers[2])
    
    # If no equation is found, return None
    return None

