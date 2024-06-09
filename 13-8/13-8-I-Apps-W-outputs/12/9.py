
def solve(n, k):
    # Initialize variables to store the numbers of winners, diplomas, and certificates
    winners, diplomas, certificates = 0, 0, 0
    
    # Loop through the possible numbers of winners
    for winners in range(n//2+1):
        # Calculate the number of diplomas and certificates for this number of winners
        diplomas = winners
        certificates = winners * k
        
        # Check if the number of certificates is not greater than the number of students
        if certificates <= n:
            # Break the loop if the number of winners is maximum possible
            if winners == n//2:
                break
    
    # Calculate the number of students who are not winners
    not_winners = n - winners
    
    # Return the results
    return (diplomas, certificates, not_winners)

