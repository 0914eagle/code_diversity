
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Initialize the equation with the first two numbers
    equation = str(numbers[0]) + "+" + str(numbers[1])
    # Check if the third number is a valid solution for the equation
    if numbers[2] == int(eval(equation)):
        return equation + "=" + str(numbers[2])
    # If not, try with subtraction
    equation = str(numbers[0]) + "-" + str(numbers[1])
    if numbers[2] == int(eval(equation)):
        return equation + "=" + str(numbers[2])
    # If not, try with multiplication
    equation = str(numbers[0]) + "*" + str(numbers[1])
    if numbers[2] == int(eval(equation)):
        return equation + "=" + str(numbers[2])
    # If not, try with division
    equation = str(numbers[0]) + "/" + str(numbers[1])
    if numbers[2] == int(eval(equation)):
        return equation + "=" + str(numbers[2])
    # If none of the above conditions are met, return "Impossible"
    return "Impossible"

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

