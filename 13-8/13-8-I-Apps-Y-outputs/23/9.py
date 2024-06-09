
def solve(a):
    n = len(a)
    if n == 0:
        return "YES", 0, [], n, a
    if n == 1:
        return "YES", 1, [a[0]], 0, []
    
    # find the first increasing and decreasing subsequences
    inc_seq = [a[0]]
    dec_seq = [a[0]]
    for i in range(1, n):
        if a[i] > a[i-1]:
            inc_seq.append(a[i])
        elif a[i] < a[i-1]:
            dec_seq.append(a[i])
    
    # check if the sequences are valid
    if len(inc_seq) == 0 or len(dec_seq) == 0:
        return "NO", 0, [], 0, []
    
    # find the longest common subsequence of the two sequences
    lcs = []
    for i in range(min(len(inc_seq), len(dec_seq))):
        if inc_seq[i] == dec_seq[i]:
            lcs.append(inc_seq[i])
    
    # check if the LCS is a prefix of both sequences
    if inc_seq[:len(lcs)] != lcs or dec_seq[:len(lcs)] != lcs:
        return "NO", 0, [], 0, []
    
    # return the result
    return "YES", len(lcs), lcs, len(inc_seq) - len(lcs), inc_seq[len(lcs):]

