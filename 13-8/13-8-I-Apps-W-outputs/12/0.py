
def solve(n, k):
    # Initialize variables to track the number of winners, diplomas, and certificates
    num_winners = 0
    num_diplomas = 0
    num_certificates = 0

    # Loop through each student and check if they are a winner
    for i in range(1, n+1):
        # Check if the current student is a winner
        if num_winners < n//2 and num_diplomas < num_certificates*k:
            num_winners += 1
            num_diplomas += 1
            num_certificates += k
        else:
            num_diplomas += 1

    # Calculate the number of non-winners
    num_non_winners = n - num_winners

    # Return the results
    return num_diplomas, num_certificates, num_non_winners

