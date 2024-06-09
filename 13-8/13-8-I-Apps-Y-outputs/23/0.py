
def solve(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    inc_seq = []
    dec_seq = []
    for i in range(n):
        if a[i] > a[(i+1)%n]:
            dec_seq.append(a[i])
        elif a[i] < a[(i+1)%n]:
            inc_seq.append(a[i])
    
    if len(inc_seq) == 0 and len(dec_seq) == 0:
        return "NO"
    
    return "YES"

