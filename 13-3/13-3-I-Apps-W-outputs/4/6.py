
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
    
    # Convert integers to lists of digits
    while x > 0:
        x_digits.append(x % 10)
        x //= 10
    while y > 0:
        y_digits.append(y % 10)
        y //= 10
    
    # Alternate digits of x and y
    while len(x_digits) > 0 or len(y_digits) > 0:
        if len(x_digits) > 0:
            result.append(x_digits.pop())
        if len(y_digits) > 0:
            result.append(y_digits.pop())
    
    # Convert list of digits back to integer
    result = int("".join(map(str, result)))
    return result

