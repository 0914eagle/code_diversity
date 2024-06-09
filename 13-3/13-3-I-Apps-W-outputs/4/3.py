
def solve(n, arr):
    # Calculate the sum of all pairs of numbers
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += f(arr[i], arr[j])
    # Return the result modulo 998244353
    return sum % 998244353

# Function to alternate the digits of two numbers
def f(x, y):
    # Initialize the result
    result = ""
    # Loop through the digits of x and y
    for i in range(len(str(x))):
        # Add the digit of x to the result
        result += str(x)[i]
        # If there are still digits in y, add the next digit of y to the result
        if i < len(str(y)):
            result += str(y)[i]
    # Return the result
    return int(result)

