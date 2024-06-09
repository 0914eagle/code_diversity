
def get_min_mex(subarrays):
    mex = 0
    for subarray in subarrays:
        for i in range(subarray[0], subarray[1] + 1):
            if i not in subarray:
                mex = max(mex, i)
    return mex


def solve(n, m):
    subarrays = []
    for i in range(m):
        l, r = map(int, input().split())
        subarrays.append([l, r])

    a = [0] * n
    for i in range(n):
        a[i] = i + 1

    min_mex = get_min_mex(subarrays)
    for i in range(n):
        if a[i] != 0:
            a[i] = min_mex
            min_mex += 1

    print(min_mex)
    print(*a)


n, m = map(int, input().split())
solve(n, m)

