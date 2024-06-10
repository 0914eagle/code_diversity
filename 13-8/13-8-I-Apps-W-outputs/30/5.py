
def get_max_number(v, a):
    # Initialize variables
    max_number = 0
    current_number = 0
    current_paint = 0

    # Iterate through the given numbers
    for i in range(1, 10):
        # Calculate the current number
        current_number = current_number * 10 + i

        # Calculate the current paint required
        current_paint = current_paint + a[i - 1]

        # Check if the current paint is less than or equal to the given amount of paint
        if current_paint <= v:
            # If it is, update the maximum number
            max_number = current_number
        else:
            # If it is not, break the loop
            break

    # Return the maximum number
    return max_number

def main():
    # Read the input
    v = int(input())
    a = list(map(int, input().split()))

    # Call the get_max_number function
    max_number = get_max_number(v, a)

    # Print the result
    print(max_number)

if __name__ == '__main__':
    main()

