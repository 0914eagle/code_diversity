
def solve(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = n

    # Loop until we find the maximum possible number of winners
    while diplomas + certificates <= n // 2:
        diplomas += 1
        certificates += k
        non_winners = n - diplomas - certificates

    # Return the results
    return diplomas, certificates, non_winners

