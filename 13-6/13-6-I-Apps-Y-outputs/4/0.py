
def get_remainder(number, x, y):
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(number)]
    # Initialize the remainder and the number of operations
    remainder = 0
    operations = 0
    # Iterate through the digits of the number
    for i in range(len(digits)):
        # Calculate the current remainder
        remainder = (remainder * 2 + digits[i]) % 10
        # If the current remainder is equal to y, return the number of operations
        if remainder == y:
            return operations
        # If the current remainder is equal to 0 and the current digit is 0, change the digit to 1 and increment the number of operations
        if remainder == 0 and digits[i] == 0:
            digits[i] = 1
            operations += 1
    # If the remainder is not equal to y after iterating through all the digits, return -1
    return -1

def main():
    n, x, y = map(int, input().split())
    number = int(input())
    print(get_remainder(number, x, y))

if __name__ == '__main__':
    main()

