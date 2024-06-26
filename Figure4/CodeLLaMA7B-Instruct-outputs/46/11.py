


def fib4(n: int):
    
    # Initialize a list to store the Fib4 sequence
    fib4_seq = [0, 0, 2]

    # Loop through the range of n-3 to 0
    for i in range(3, n+1):
        # Add the previous four terms of the sequence
        fib4_seq.append(fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4])

    # Return the n-th term of the sequence
    return fib4_seq[n]


