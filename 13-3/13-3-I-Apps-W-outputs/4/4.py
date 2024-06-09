
def solve(n, arr):
    # Calculate the sum of all pairs of numbers
    sum = 0
    for i in range(n):
        for j in range(i, n):
            sum += f(arr[i], arr[j])
    # Return the result modulo 998244353
    return sum % 998244353

# Function to alternate digits of two numbers
def f(x, y):
    # Initialize variables
    x_digits = []
    y_digits = []
    result = []
    # Split the digits of x and y into two lists
    while x > 0:
        x_digits.append(x % 10)
        x //= 10
    while y > 0:
        y_digits.append(y % 10)
        y //= 10
    # Alternate the digits of x and y
    while len(x_digits) > 0 and len(y_digits) > 0:
        result.append(x_digits.pop())
        result.append(y_digits.pop())
    # If one number has more digits than the other, add the remaining digits
    while len(x_digits) > 0:
        result.append(x_digits.pop())
    while len(y_digits) > 0:
        result.append(y_digits.pop())
    # Return the result as an integer
    return int("".join(map(str, result)))

