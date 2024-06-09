
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
        b[i] = find_mex(a[:i+1])
    return b

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = solve(n, a)
    if b == [-1]:
        print(-1)
    else:
        print(*b)

