
def buy_integer(A, B, X):
    # Initialize variables
    max_integer = 0
    max_value = 0

    # Iterate through each integer from 1 to 10^9
    for i in range(1, 10**9 + 1):
        # Calculate the value of the integer
        value = A * i + B * len(str(i))

        # If the value is less than or equal to X and greater than the current maximum value, update the maximum value and maximum integer
        if value <= X and value > max_value:
            max_value = value
            max_integer = i

    # Return the maximum integer that can be bought
    return max_integer

def main():
    # Read input from stdin
    A, B, X = map(int, input().split())

    # Call the buy_integer function and print the result
    print(buy_integer(A, B, X))

if __name__ == '__main__':
    main()

