
def get_remainder(n, x, y):
    # Initialize the number with the given digits
    number = n
    # Initialize the number of operations to 0
    operations = 0
    # Loop until the number has remainder y modulo x
    while number % (10**x) != (10**y):
        # Find the first digit that is not 1
        first_non_one = number.find("0")
        # If all digits are 1, then change the first digit to 0
        if first_non_one == -1:
            number = "0" + number[1:]
        # Otherwise, change the first non-one digit to 1
        else:
            number = number[:first_non_one] + "1" + number[first_non_one+1:]
        # Increment the number of operations
        operations += 1
    # Return the minimum number of operations
    return operations

def main():
    n, x, y = map(int, input().split())
    print(get_remainder(input(), x, y))

if __name__ == '__main__':
    main()

