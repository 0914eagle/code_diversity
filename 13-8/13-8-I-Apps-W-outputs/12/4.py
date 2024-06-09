
def get_winners(n, k):
    # Initialize variables to track the number of winners, diplomas, and certificates
    winners, diplomas, certificates = 0, 0, 0
    
    # Loop through the students and award them based on the rules
    for i in range(n):
        if winners < n//2:
            if diplomas < certificates * k:
                diplomas += 1
                winners += 1
            else:
                certificates += 1
                winners += 1
        else:
            break
    
    # Calculate the number of non-winners
    non_winners = n - winners
    
    # Return the results
    return diplomas, certificates, non_winners

