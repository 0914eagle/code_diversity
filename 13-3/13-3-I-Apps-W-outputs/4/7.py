
def solve(n, arr):
    # Calculate the sum of all pairs of numbers
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += f(arr[i], arr[j])
    
    # Return the sum modulo 998244353
    return sum % 998244353

def f(x, y):
    # Initialize the result
    result = ""
    
    # Iterate through the digits of x and y
    i, j = 0, 0
    while i < len(x) and j < len(y):
        # Append the digit of x to the result
        result += x[i]
        # Append the digit of y to the result
        result += y[j]
        # Increment the indices
        i += 1
        j += 1
    
    # If x has more digits than y, append the remaining digits of x to the result
    while i < len(x):
        result += x[i]
        i += 1
    
    # If y has more digits than x, append the remaining digits of y to the result
    while j < len(y):
        result += y[j]
        j += 1
    
    # Return the result
    return result

