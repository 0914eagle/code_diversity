
def get_min_operations(n, x, y, number):
    # Initialize variables
    operations = 0
    remainder = 1

    # Iterate through the digits of the number
    for i in range(n):
        # If the current digit is 0, change it to 1 and increment the operations count
        if number[i] == "0":
            number = number[:i] + "1" + number[i+1:]
            operations += 1
        # If the current digit is 1, change it to 0 and calculate the remainder
        else:
            remainder = (remainder * 10) % (10**x)

    # Return the minimum number of operations needed to obtain the desired remainder
    return operations + (10**y - remainder) // (10**(y-1))

def main():
    n, x, y = map(int, input().split())
    number = input()
    print(get_min_operations(n, x, y, number))

if __name__ == '__main__':
    main()

