
def get_winners(n, k):
    # Initialize variables
    diplomas = 0
    certificates = 0
    non_winners = n

    # Loop through possible numbers of diplomas
    for d in range(n//2+1):
        # Calculate number of certificates
        c = k*d

        # Check if number of certificates is less than or equal to half of the number of students
        if c <= n//2:
            # Calculate number of non-winners
            non_winners = n - d - c

            # Check if number of non-winners is non-negative
            if non_winners >= 0:
                # Update variables
                diplomas = d
                certificates = c
                break

    return diplomas, certificates, non_winners

