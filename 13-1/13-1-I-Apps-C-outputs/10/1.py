
def get_kth_sequence(n, k):
    # Initialize a list to store the sequence
    sequence = []
    # Set a counter for the number of sequences found
    count = 0
    # Iterate through the possible values of the first flower
    for i in range(1, n):
        # If the first flower has i petals, then the second flower must have at least 1 petal
        for j in range(1, n-i+1):
            # If the second flower has j petals, then the third flower must have at least 1 petal
            for k in range(1, n-i-j+1):
                # If the third flower has k petals, then the fourth flower must have at least 1 petal
                for l in range(1, n-i-j-k+1):
                    # If the fourth flower has l petals, then the sequence is valid
                    if l == n-i-j-k-l:
                        # Increment the counter
                        count += 1
                        # If the counter is equal to k, then return the sequence
                        if count == k:
                            return [i, j, k, l]
    # If no sequence is found, return an empty list
    return []

