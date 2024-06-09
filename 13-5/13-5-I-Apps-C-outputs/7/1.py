
def get_min_mex(subarrays):
    mex = 0
    for subarray in subarrays:
        for i in range(subarray[0], subarray[1] + 1):
            if i not in subarray:
                mex = max(mex, i)
    return mex


def get_optimal_array(n, m):
    subarrays = []
    for i in range(m):
        l, r = map(int, input().split())
        subarrays.append([l, r])

    a = [0] * n
    for i in range(n):
        a[i] = i + 1

    min_mex = get_min_mex(subarrays)
    return min_mex, a


n, m = map(int, input().split())
min_mex, a = get_optimal_array(n, m)
print(min_mex)
print(*a)

