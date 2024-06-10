
def get_largest_integer(A, B, X):
    # Initialize variables
    max_integer = 0
    current_price = 0

    # Iterate through each integer from 1 to 10^9
    for i in range(1, 10**9 + 1):
        # Calculate the price of the current integer
        current_price = A * i + B * len(str(i))

        # If the current price is less than or equal to the given X, update the max integer
        if current_price <= X:
            max_integer = i

    # Return the largest integer that can be bought
    return max_integer

def main():
    # Read inputs from stdin
    A, B, X = map(int, input().split())

    # Call the get_largest_integer function and print the result
    print(get_largest_integer(A, B, X))

if __name__ == '__main__':
    main()

