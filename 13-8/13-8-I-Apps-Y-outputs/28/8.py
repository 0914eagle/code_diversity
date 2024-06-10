
def solve(numbers):
    # Split the input string into a list of integers
    numbers = [int(x) for x in numbers.split()]
    
    # Create a list of all possible operations
    operations = ['+', '-', '*', '/']
    
    # Iterate over the possible operations
    for operation in operations:
        # Check if the equation is valid
        if eval(f"{numbers[0]} {operation} {numbers[1]} == {numbers[2]}"):
            # If the equation is valid, return it
            return f"{numbers[0]} {operation} {numbers[1]} = {numbers[2]}"
    
    # If no valid equation is found, return None
    return None

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(solve(numbers))

if __name__ == '__main__':
    main()

