
def solve(n, k, c):
    # Check if k is one of the ancient numbers
    if k in c:
        return "Yes"
    
    # Check if any two ancient numbers have a common factor greater than 1
    for i in range(n):
        for j in range(i+1, n):
            if __gcd(c[i], c[j]) > 1:
                return "No"
    
    # If all ancient numbers are pairwise coprime, then Arya has a winning strategy
    return "Yes"

