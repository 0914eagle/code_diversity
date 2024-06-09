
def solve(n, arr):
    # Calculate the sum of all pairs of numbers
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += f(arr[i], arr[j])
    
    # Return the result modulo 998244353
    return sum % 998244353

def f(x, y):
    # Initialize the result
    result = ""
    
    # Iterate through the digits of x and y
    i, j = 0, 0
    while i < len(x) and j < len(y):
        # Add the digits of x and y alternately to the result
        result += str(int(x[i]) + int(y[j]))
        i += 1
        j += 1
    
    # If x has more digits than y, add the remaining digits of x to the result
    while i < len(x):
        result += str(int(x[i]))
        i += 1
    
    # If y has more digits than x, add the remaining digits of y to the result
    while j < len(y):
        result += str(int(y[j]))
        j += 1
    
    # Return the result as an integer
    return int(result)

