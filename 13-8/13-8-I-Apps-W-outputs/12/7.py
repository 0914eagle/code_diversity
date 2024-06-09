
def solve(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = 0
    
    # Loop through possible combinations of diplomas and certificates
    for d in range(n//2+1):
        c = k*d
        if c <= n-d:
            non_winners = n-d-c
            if non_winners <= n//2:
                diplomas = d
                certificates = c
                break
    
    # Return results
    return diplomas, certificates, non_winners

