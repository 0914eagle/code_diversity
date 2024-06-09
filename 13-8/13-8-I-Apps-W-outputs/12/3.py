
def get_max_winners(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = n
    
    # Loop until the number of winners is maximum possible
    while diplomas + certificates < non_winners // 2:
        diplomas += 1
        certificates += k
        non_winners -= 1
    
    # Return the results
    return (diplomas, certificates, non_winners)

