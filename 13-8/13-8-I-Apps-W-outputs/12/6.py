
def solve(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = n

    # Loop until the number of winners is maximum possible
    while diplomas + certificates <= non_winners // 2:
        # Calculate the number of winners with diplomas
        diplomas += 1
        certificates = k * diplomas

        # Calculate the number of winners with certificates
        certificates += 1
        non_winners = n - diplomas - certificates

    # Return the results
    return diplomas, certificates, non_winners

