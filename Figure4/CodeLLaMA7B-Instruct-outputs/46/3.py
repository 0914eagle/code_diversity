


def fib4(n: int):
    
    # Initialize a list to store the Fib4 sequence
    fib4_seq = [0, 0, 2]

    # Loop through the range of values from 3 to n
    for i in range(3, n+1):
        # Add the previous four terms of the sequence to get the current term
        fib4_seq.append(fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4])

    # Return the n-th term of the Fib4 sequence
    return fib4_seq[n]


