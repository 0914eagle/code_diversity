
def get_max_number(v, a):
    # Initialize variables
    max_number = 0
    remaining_paint = v

    # Loop through the list of numbers
    for i in range(len(a)):
        # Calculate the current number
        current_number = a[i] * (10 ** i)

        # Check if the current number is possible with the remaining paint
        if current_number <= remaining_paint:
            # Add the current number to the maximum number
            max_number += current_number

            # Subtract the current number from the remaining paint
            remaining_paint -= current_number
        else:
            # If the current number is not possible, break the loop
            break

    # Return the maximum number
    return max_number

def main():
    # Take input
    v = int(input())
    a = list(map(int, input().split()))

    # Call the get_max_number function
    max_number = get_max_number(v, a)

    # Print the maximum number
    print(max_number)

if __name__ == '__main__':
    main()

