
def get_largest_integer(A, B, X):
    # Initialize variables
    max_integer = 0
    max_integer_value = 0

    # Iterate through integers from 1 to 10^9
    for i in range(1, 10**9 + 1):
        # Calculate the value of the current integer
        value = A * i + B * len(str(i))

        # Check if the current integer is the largest that can be bought with X yen
        if value <= X:
            max_integer = i
            max_integer_value = value

    # Return the largest integer that can be bought with X yen
    return max_integer

def main():
    # Read input from stdin
    A, B, X = map(int, input().split())

    # Call get_largest_integer function
    largest_integer = get_largest_integer(A, B, X)

    # Print the result
    print(largest_integer)

if __name__ == '__main__':
    main()

