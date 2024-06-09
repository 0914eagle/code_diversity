
def get_mex(arr):
    mex = 0
    for i in range(len(arr)):
        if arr[i] != mex:
            return mex
        mex += 1
    return mex + 1

def solve(arr):
    n = len(arr)
    b = [0] * n
    for i in range(n):
        b[i] = get_mex(b[:i] + [arr[i]])
    return b

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    b = solve(arr)
    if b == [-1]:
        print(-1)
    else:
        print(*b)

