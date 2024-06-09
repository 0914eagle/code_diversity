
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
    # Loop through the digits of x and y alternately
    for i in range(max(len(str(x)), len(str(y)))):
        # If i is even, add the digit from x
        if i % 2 == 0:
            result += str(x % 10)
            x //= 10
        # If i is odd, add the digit from y
        else:
            result += str(y % 10)
            y //= 10
    # Return the result
    return int(result[::-1])

