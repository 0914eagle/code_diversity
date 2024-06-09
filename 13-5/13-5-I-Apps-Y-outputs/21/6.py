
def f1(n, a):
    # find the longest increasing subsequence
    lis = [0] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    # find the longest decreasing subsequence
    lds = [0] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if a[i] > a[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    # check if the sum of LIS and LDS is equal to n
    if sum(lis) + sum(lds) == n:
        return True
    else:
        return False

def f2(n, a):
    # find the longest increasing subsequence
    lis = [0] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    # find the longest decreasing subsequence
    lds = [0] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if a[i] > a[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    # construct the resulting sequence
    res = [0] * n
    for i in range(n):
        if lis[i] > 0:
            res[i] = 0
        else:
            res[i] = 1
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if f1(n, a):
        print("YES")
        print(*f2(n, a))
    else:
        print("NO")

