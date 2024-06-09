
def get_min_operations(n, x, y, number):
    # Initialize variables
    operations = 0
    remainder = 1

    # Iterate through the digits of the number
    for i in range(n):
        # If the current digit is 0, flip it to 1
        if number[i] == "0":
            number = number[:i] + "1" + number[i+1:]
            operations += 1

        # If the current digit is 1, flip it to 0
        elif number[i] == "1":
            number = number[:i] + "0" + number[i+1:]
            operations += 1

        # If the current digit is 0, flip it to 1
        if number[i] == "0":
            number = number[:i] + "1" + number[i+1:]
            operations += 1

        # If the current digit is 1, flip it to 0
        elif number[i] == "1":
            number = number[:i] + "0" + number[i+1:]
            operations += 1

        # Calculate the remainder of the number divided by 10^x
        remainder = int(number) % (10**x)

        # If the remainder is equal to 10^y, return the current number of operations
        if remainder == (10**y):
            return operations

    # If the number has not been transformed into a number with remainder 10^y modulo 10^x, return -1
    return -1

def main():
    n, x, y = map(int, input().split())
    number = input()
    print(get_min_operations(n, x, y, number))

if __name__ == '__main__':
    main()

