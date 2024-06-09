
def solve(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = 0

    # Loop through possible combinations of diplomas and certificates
    for d in range(n + 1):
        for c in range(k * d, (k * d) + 1):
            # Check if the number of winners is less than or equal to half of the total number of students
            if d + c <= n / 2:
                # Update variables
                diplomas = d
                certificates = c
                non_winners = n - (d + c)
                break

    # Return results
    return diplomas, certificates, non_winners

