
def solve(n, k, c):
    # Check if k is one of the ancient numbers
    if k in c:
        return "Yes"
    
    # Check if any two ancient numbers have a common factor greater than 1
    for i in range(n):
        for j in range(i+1, n):
            if __gcd(c[i], c[j]) > 1:
                return "Yes"
    
    # If both conditions above are not met, then Arya does not have a winning strategy
    return "No"

