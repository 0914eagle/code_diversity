
def find_sequences(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    # initialize the increasing and decreasing sequences
    inc_seq = []
    dec_seq = []
    
    # iterate through the elements of a
    for i in range(n):
        # if the element is greater than the last element of the increasing sequence, add it to the increasing sequence
        if len(inc_seq) == 0 or inc_seq[-1] < a[i]:
            inc_seq.append(a[i])
        # if the element is less than the last element of the decreasing sequence, add it to the decreasing sequence
        elif len(dec_seq) == 0 or dec_seq[-1] > a[i]:
            dec_seq.append(a[i])
        # if the element is already in the increasing or decreasing sequence, return "NO"
        else:
            return "NO"
    
    # return "YES" and the increasing and decreasing sequences
    return "YES", inc_seq, dec_seq

