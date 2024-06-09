
def get_initial_sequences(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    # Initialize the increasing and decreasing sequences
    inc_seq = []
    dec_seq = []
    
    # Add the first element to the increasing sequence
    inc_seq.append(a[0])
    
    # Add the first element to the decreasing sequence
    dec_seq.append(a[0])
    
    # Iterate through the remaining elements
    for i in range(1, n):
        # If the current element is greater than the last element of the increasing sequence, add it to the increasing sequence
        if a[i] > inc_seq[-1]:
            inc_seq.append(a[i])
        # If the current element is less than the last element of the decreasing sequence, add it to the decreasing sequence
        elif a[i] < dec_seq[-1]:
            dec_seq.append(a[i])
        # If the current element is equal to the last element of both sequences, do nothing
        else:
            pass
    
    # If the increasing sequence is empty, return "NO"
    if len(inc_seq) == 0:
        return "NO"
    
    # If the decreasing sequence is empty, return "NO"
    if len(dec_seq) == 0:
        return "NO"
    
    # Return "YES" and the increasing and decreasing sequences
    return "YES", inc_seq, dec_seq

