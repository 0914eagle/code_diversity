
def get_initial_sequences(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    inc_seq = []
    dec_seq = []
    for i in range(n):
        if i == 0:
            inc_seq.append(a[i])
            dec_seq.append(a[i])
        elif a[i] > inc_seq[-1]:
            inc_seq.append(a[i])
        elif a[i] < dec_seq[-1]:
            dec_seq.append(a[i])
        else:
            return "NO"
    
    return "YES", inc_seq, dec_seq

