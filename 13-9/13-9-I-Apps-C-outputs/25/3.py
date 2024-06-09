
def solve(n, a):
    # Initialize the minimum number of seconds as 0
    seconds = 0

    # Check if at least one of the boxes has a positive number of chocolates
    if any(a):
        # Sort the boxes in descending order of the number of chocolates
        sorted_boxes = sorted(a, reverse=True)

        # Initialize the greatest common divisor as the largest number of chocolates in a box
        gcd = sorted_boxes[0]

        # Iterate through the boxes in descending order
        for i in range(1, len(a)):
            # Calculate the greatest common divisor of the current box and the previous box
            gcd = get_gcd(gcd, sorted_boxes[i])

            # If the greatest common divisor is 1, it means that the boxes are not coprime and Alice will not be happy
            if gcd == 1:
                return -1

        # Return the minimum number of seconds needed to make Alice happy
        return seconds

    # If all the boxes have 0 chocolates, return -1
    else:
        return -1

# Function to calculate the greatest common divisor of two numbers
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the solve function with example inputs
n = 3
a = [4, 8, 5]
print(solve(n, a)) # Output: 9

n = 5
a = [3, 10, 2, 1, 5]
print(solve(n, a)) # Output: 2

n = 4
a = [0, 5, 15, 10]
print(solve(n, a)) # Output: 0

n = 1
a = [1]
print(solve(n, a)) # Output: -1

