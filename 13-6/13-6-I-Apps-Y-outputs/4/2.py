
def get_remainder(n, x, y):
    # Initialize the number with the given digits
    number = n
    # Initialize the number of operations to 0
    operations = 0
    # Loop until the number has remainder y modulo x
    while number % (10**x) != (10**y):
        # Find the first digit that is not 0
        first_nonzero_digit = 0
        while number % 10 == 0:
            number //= 10
            first_nonzero_digit += 1
        # Change the first nonzero digit to 0 if it is 1, or to 1 if it is 0
        if number % 10 == 1:
            number = number - 10**first_nonzero_digit
        else:
            number = number + 10**first_nonzero_digit
        # Increment the number of operations
        operations += 1
    # Return the minimum number of operations
    return operations

def main():
    n, x, y = map(int, input().split())
    print(get_remainder(n, x, y))

if __name__ == '__main__':
    main()

