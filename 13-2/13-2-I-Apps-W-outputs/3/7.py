
def find_mex(arr):
    n = len(arr)
    mex = 0
    for i in range(n):
        if arr[i] != mex:
            return mex
        mex += 1
    return mex + 1

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = find_mex(b[:i+1])
        if b[i] != a[i]:
            return [-1]
    return b

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(n, a))

