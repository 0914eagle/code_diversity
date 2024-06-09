
def get_mex(arr):
    mex = 0
    for i in range(len(arr)):
        if arr[i] != mex:
            return mex
        mex += 1
    return mex + 1

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = get_mex(b[:i] + a[i+1:])
    return b

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = solve(n, a)
    if b == [-1]:
        print(-1)
    else:
        print(*b)

