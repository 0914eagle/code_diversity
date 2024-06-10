
def bitwise_and_or_game(a, b):
    # Initialize the minimum value to a large number
    min_value = 2 ** 9 - 1
    # Loop through each element in a
    for i in range(len(a)):
        # Initialize the current value to 0
        current_value = 0
        # Loop through each element in b
        for j in range(len(b)):
            # Calculate the bitwise AND of a[i] and b[j]
            and_value = a[i] & b[j]
            # Calculate the bitwise OR of current_value and and_value
            current_value |= and_value
        # Update the minimum value if the current value is smaller
        if current_value < min_value:
            min_value = current_value
    # Return the minimum value
    return min_value

def main():
    # Read the input data
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Solve the problem
    result = bitwise_and_or_game(a, b)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

