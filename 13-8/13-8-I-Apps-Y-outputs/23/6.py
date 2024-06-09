
def find_sequences(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    inc_seq = []
    dec_seq = []
    for i in range(n):
        if a[i] not in inc_seq and a[i] not in dec_seq:
            inc_seq.append(a[i])
        if a[n-i-1] not in inc_seq and a[n-i-1] not in dec_seq:
            dec_seq.append(a[n-i-1])
    
    inc_seq.sort()
    dec_seq.sort(reverse=True)
    
    if len(inc_seq) + len(dec_seq) != n:
        return "NO"
    
    return "YES\n" + str(len(inc_seq)) + "\n" + " ".join(str(x) for x in inc_seq) + "\n" + str(len(dec_seq)) + "\n" + " ".join(str(x) for x in dec_seq)

