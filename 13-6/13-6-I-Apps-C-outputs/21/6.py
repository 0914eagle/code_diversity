
def solve(n, k, c):
    # Check if k is one of the ancient numbers
    if k in c:
        return "Yes"
    
    # Check if any two ancient numbers have a common remainder
    for i in range(n):
        for j in range(i+1, n):
            if c[i] % k == c[j] % k:
                return "Yes"
    
    return "No"

