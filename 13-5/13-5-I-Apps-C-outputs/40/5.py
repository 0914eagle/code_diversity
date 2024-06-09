
def f1(n, k, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    starting_circles = {}

    # Iterate through all possible starting circles
    for i in range(2**n):
        # Convert the binary representation of i to a binary string with n digits
        binary_string = bin(i)[2:].zfill(n)

        # Initialize a list to store the current circle
        current_circle = []

        # Iterate through each digit of the binary string
        for j in range(n):
            # If the digit is 0, add a black pebble to the current circle
            if binary_string[j] == "0":
                current_circle.append("B")
            # If the digit is 1, add a white pebble to the current circle
            else:
                current_circle.append("W")

        # Add the current circle to the starting circles dictionary
        starting_circles[tuple(current_circle)] = starting_circles.get(tuple(current_circle), 0) + 1

    # Return the number of distinct starting circles
    return len(starting_circles)

def f2(n, k, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    starting_circles = {}

    # Iterate through all possible starting circles
    for i in range(2**n):
        # Convert the binary representation of i to a binary string with n digits
        binary_string = bin(i)[2:].zfill(n)

        # Initialize a list to store the current circle
        current_circle = []

        # Iterate through each digit of the binary string
        for j in range(n):
            # If the digit is 0, add a black pebble to the current circle
            if binary_string[j] == "0":
                current_circle.append("B")
            # If the digit is 1, add a white pebble to the current circle
            else:
                current_circle.append("W")

        # Add the current circle to the starting circles dictionary
        starting_circles[tuple(current_circle)] = starting_circles.get(tuple(current_circle), 0) + 1

    # Return the number of distinct starting circles
    return len(starting_circles)

if __name__ == '__main__':
    n, k = map(int, input().split())
    circle = list(input())
    print(f1(n, k, circle))
    print(f2(n, k, circle))

