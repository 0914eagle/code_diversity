
def get_max_number(paint, a):
    # Initialize variables
    max_number = 0
    curr_paint = 0
    i = 1

    # Iterate through the array of a
    while i <= 9 and curr_paint <= paint:
        # Calculate the current number
        curr_number = a[i-1] * i

        # Check if the current number is greater than the maximum number
        if curr_number > max_number:
            max_number = curr_number

        # Increment the current paint
        curr_paint += a[i-1]

        # Increment the loop variable
        i += 1

    # Return the maximum number
    return max_number

def main():
    # Read input
    paint = int(input())
    a = list(map(int, input().split()))

    # Call the function to get the maximum number
    max_number = get_max_number(paint, a)

    # Print the output
    print(max_number)

if __name__ == '__main__':
    main()

