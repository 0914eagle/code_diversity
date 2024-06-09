
def get_kth_sequence(n, k):
    # Initialize a list to store the sequence
    sequence = []
    # Loop through the numbers from 1 to n-1
    for i in range(1, n):
        # Check if the current number is a multiple of n
        if i % n != 0:
            # If it's not a multiple, add it to the sequence
            sequence.append(i)
            # Decrement k
            k -= 1
        # If k is 0, break the loop
        if k == 0:
            break
    # Return the sequence
    return sequence

