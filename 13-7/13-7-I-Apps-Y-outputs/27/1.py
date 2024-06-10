
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Get the unique numbers from the list
    unique_numbers = set(numbers)
    # Iterate over the unique numbers
    for num1 in unique_numbers:
        for num2 in unique_numbers:
            if num1 + num2 in unique_numbers:
                return str(num1) + "+" + str(num2) + "=" + str(num1 + num2)
            elif num1 - num2 in unique_numbers:
                return str(num1) + "-" + str(num2) + "=" + str(num1 - num2)
            elif num1 * num2 in unique_numbers:
                return str(num1) + "*" + str(num2) + "=" + str(num1 * num2)
            elif num1 / num2 in unique_numbers:
                return str(num1) + "/" + str(num2) + "=" + str(num1 / num2)
    return "No solution found"

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

