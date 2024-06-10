
def get_greatest_integer_below_x(A, B, X):
    # Initialize variables
    max_integer = 0
    current_integer = 1
    current_price = A * current_integer + B * len(str(current_integer))

    # Loop through integers from 1 to 10^9
    while current_price <= X:
        max_integer = current_integer
        current_integer += 1
        current_price = A * current_integer + B * len(str(current_integer))

    return max_integer

def main():
    # Take input from stdin
    A, B, X = map(int, input().split())

    # Call the function to get the greatest integer below X
    max_integer = get_greatest_integer_below_x(A, B, X)

    # Print the result
    print(max_integer)

if __name__ == '__main__':
    main()

