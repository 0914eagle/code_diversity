
def solve_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Sort the numbers in ascending order
    numbers.sort()
    # Find the equation by trying all possible operations
    for op in ['+', '-', '*', '/']:
        # Check if the equation is valid
        if eval(f"{numbers[0]}{op}{numbers[1]}") == numbers[2]:
            return f"{numbers[0]} {op} {numbers[1]} = {numbers[2]}"
    # If no equation is found, return None
    return None

def main():
    numbers = input("Enter three integers separated by spaces: ")
    equation = solve_equation(numbers)
    if equation:
        print(equation)
    else:
        print("No equation found.")

if __name__ == '__main__':
    main()

