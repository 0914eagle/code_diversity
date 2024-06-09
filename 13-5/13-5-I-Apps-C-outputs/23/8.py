
def f1(n, seq):
    # find the longest increasing subsequence (LIS) of the given sequence
    lis = []
    for i in range(n):
        if not lis or seq[i] > lis[-1]:
            lis.append(seq[i])
    return lis

def f2(n, seq, lis):
    # find all critical elements in the sequence
    critical_elements = []
    for i in range(n):
        if seq[i] not in lis:
            continue
        # remove the current element from the LIS and check if the length decreases
        lis_copy = lis.copy()
        lis_copy.remove(seq[i])
        if len(lis_copy) < len(lis):
            critical_elements.append(seq[i])
    return critical_elements

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    lis = f1(n, seq)
    critical_elements = f2(n, seq, lis)
    if not critical_elements:
        print(-1)
    else:
        print(*critical_elements)

