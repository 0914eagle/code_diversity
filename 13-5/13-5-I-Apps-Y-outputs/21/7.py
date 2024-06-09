
def f1(a):
    # find the longest increasing subsequence
    longest_inc_subseq = []
    for i in range(len(a)):
        if not longest_inc_subseq or longest_inc_subseq[-1] < a[i]:
            longest_inc_subseq.append(a[i])
    return longest_inc_subseq

def f2(a):
    # find the longest decreasing subsequence
    longest_dec_subseq = []
    for i in range(len(a)-1, -1, -1):
        if not longest_dec_subseq or longest_dec_subseq[-1] > a[i]:
            longest_dec_subseq.append(a[i])
    return longest_dec_subseq

def solve(a):
    inc_subseq = f1(a)
    dec_subseq = f2(a)
    if len(inc_subseq) + len(dec_subseq) != len(a):
        return "NO"
    res = [0] * len(a)
    for i in range(len(inc_subseq)):
        res[i] = 0
    for i in range(len(dec_subseq)):
        res[len(a)-i-1] = 1
    return "YES\n" + " ".join(map(str, res))

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(solve(a))

