
def solve(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = 0

    # Loop through possible number of diplomas
    for d in range(n//2+1):
        # Calculate number of certificates
        c = k*d

        # Check if number of certificates is not greater than half of the number of students
        if c <= n//2:
            # Calculate number of non-winners
            non_winners = n - d - c

            # Check if number of non-winners is not negative
            if non_winners >= 0:
                # Update variables
                diplomas = d
                certificates = c
                non_winners = non_winners
                break

    return diplomas, certificates, non_winners

