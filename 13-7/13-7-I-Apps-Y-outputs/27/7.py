
def get_equation(numbers):
    # Convert the input numbers to integers
    numbers = [int(num) for num in numbers]
    
    # Get all possible combinations of numbers and operations
    combinations = [(numbers[0], '+', numbers[1]), (numbers[0], '-', numbers[1]), (numbers[0], '*', numbers[1]), (numbers[0], '/', numbers[1])]
    
    # Iterate over the combinations and check if the equation is valid
    for combination in combinations:
        if combination[0] + combination[2] == numbers[1]:
            return f"{combination[0]} + {combination[2]} = {numbers[1]}"
        elif combination[0] - combination[2] == numbers[1]:
            return f"{combination[0]} - {combination[2]} = {numbers[1]}"
        elif combination[0] * combination[2] == numbers[1]:
            return f"{combination[0]} * {combination[2]} = {numbers[1]}"
        elif combination[0] / combination[2] == numbers[1]:
            return f"{combination[0]} / {combination[2]} = {numbers[1]}"
    
    # If no combination is valid, return None
    return None

def main():
    numbers = input("Enter three numbers separated by spaces: ").split()
    equation = get_equation(numbers)
    if equation:
        print(equation)
    else:
        print("No valid equation found.")

if __name__ == '__main__':
    main()

