
def reconstruct_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Initialize the equation with the first two numbers
    equation = str(numbers[0]) + " " + str(numbers[1]) + " "
    # Check if the third number is a multiple of the first two numbers
    if numbers[2] % numbers[0] == 0 and numbers[2] % numbers[1] == 0:
        # If it is, use multiplication
        equation += "*"
    elif numbers[0] + numbers[1] == numbers[2]:
        # If it isn't, check if the sum of the first two numbers is equal to the third number
        equation += "+"
    elif numbers[0] - numbers[1] == numbers[2]:
        # If it isn't, check if the difference of the first two numbers is equal to the third number
        equation += "-"
    else:
        # If none of the above conditions are met, use division
        equation += "/"
    # Return the completed equation
    return equation

def main():
    numbers = input("Enter three integers separated by spaces: ")
    print(reconstruct_equation(numbers))

if __name__ == '__main__':
    main()

