
def get_min_operations(n, x, y, number):
    # Initialize variables
    operations = 0
    remainder = 1

    # Iterate through the digits of the number
    for i in range(n):
        # If the current digit is 0 and the remainder is not 0, flip the digit to 1
        if number[i] == 0 and remainder != 0:
            operations += 1
            number[i] = 1

        # Calculate the new remainder
        remainder = (remainder * 10 + number[i]) % 10**x

    # Return the minimum number of operations
    return operations

def main():
    # Read the input
    n, x, y = map(int, input().split())
    number = list(map(int, input()))

    # Call the get_min_operations function and print the result
    print(get_min_operations(n, x, y, number))

if __name__ == '__main__':
    main()

