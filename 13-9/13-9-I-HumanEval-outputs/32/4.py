
def fib4(n: int) -> int:
    
    # Initialize a list to store the first 4 elements of the fib4 sequence
    fib_list = [0, 0, 2, 0]
    
    # Loop through the remaining elements of the sequence
    for i in range(4, n+1):
        # Calculate the current element of the sequence based on the previous 4 elements
        fib_list.append(fib_list[i-1] + fib_list[i-2] + fib_list[i-3] + fib_list[i-4])
    
    # Return the n-th element of the sequence
    return fib_list[n]

