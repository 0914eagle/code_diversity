
def get_remainder(number, x, y):
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(number)]
    # Initialize the remainder and the number of operations
    remainder = 0
    operations = 0
    # Iterate through the digits of the number
    for i in range(len(digits)):
        # Calculate the current remainder
        remainder = (remainder * 10 + digits[i]) % 10**x
        # If the current remainder is equal to y, return the number of operations
        if remainder == y:
            return operations
        # If the current remainder is not equal to y, increment the number of operations
        operations += 1
    # If the number has no remainder, return -1
    return -1

def main():
    # Read the input data
    n, x, y = map(int, input().split())
    number = int(input())
    # Calculate the minimum number of operations
    minimum_operations = get_remainder(number, x, y)
    # Print the minimum number of operations
    print(minimum_operations)

if __name__ == '__main__':
    main()

