
def f1(a):
    # find the longest increasing subsequence
    inc_seq = []
    for i in range(len(a)):
        if not inc_seq or inc_seq[-1] < a[i]:
            inc_seq.append(a[i])
    # find the longest decreasing subsequence
    dec_seq = []
    for i in range(len(a)-1, -1, -1):
        if not dec_seq or dec_seq[-1] > a[i]:
            dec_seq.append(a[i])
    dec_seq.reverse()
    # check if the sequence can be split into increasing and decreasing subsequence
    if len(inc_seq) + len(dec_seq) == len(a):
        return True, inc_seq, dec_seq
    else:
        return False, [], []

def f2(a):
    res = [0] * len(a)
    for i in range(len(a)):
        if a[i] in inc_seq:
            res[i] = 0
        else:
            res[i] = 1
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    flag, inc_seq, dec_seq = f1(a)
    if flag:
        print("YES")
        print(*f2(a))
    else:
        print("NO")

