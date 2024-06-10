
def get_equation(numbers):
    # Split the input numbers into a list
    numbers = numbers.split()
    # Convert the numbers to integers
    numbers = [int(num) for num in numbers]
    # Find the sum of the numbers
    sum_ = sum(numbers)
    # Find the difference of the numbers
    diff = abs(numbers[0] - numbers[1])
    # Find the product of the numbers
    product = numbers[0] * numbers[1]
    # Find the quotient of the numbers
    quotient = numbers[0] // numbers[1]
    # Check if the sum is equal to the third number
    if sum_ == numbers[2]:
        return f"{numbers[0]} + {numbers[1]} = {numbers[2]}"
    # Check if the difference is equal to the third number
    elif diff == numbers[2]:
        return f"{numbers[0]} - {numbers[1]} = {numbers[2]}"
    # Check if the product is equal to the third number
    elif product == numbers[2]:
        return f"{numbers[0]} x {numbers[1]} = {numbers[2]}"
    # Check if the quotient is equal to the third number
    elif quotient == numbers[2]:
        return f"{numbers[0]} / {numbers[1]} = {numbers[2]}"
    # If no equation is found, return None
    else:
        return None

def main():
    numbers = input("Enter three numbers separated by spaces: ")
    equation = get_equation(numbers)
    if equation:
        print(equation)
    else:
        print("No equation found.")

if __name__ == '__main__':
    main()

