
def reconstruct_equation(numbers):
    # Split the input string into a list of integers
    numbers = [int(x) for x in numbers.split()]
    
    # Iterate over the four possible operations
    for operation in ['+', '-', '*', '/']:
        # Iterate over the possible combinations of numbers and operations
        for num1 in numbers:
            for num2 in numbers:
                if num1 != num2:
                    # Check if the equation is valid
                    if eval(str(num1) + operation + str(num2)) == numbers[2]:
                        return str(num1) + operation + str(num2) + '=' + str(numbers[2])
    
    # If no valid equation is found, return None
    return None

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(reconstruct_equation(numbers))

if __name__ == '__main__':
    main()

