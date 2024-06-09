
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

    mex = get_min_mex(subarrays)
    array = [0] * n
    for i in range(n):
        if i + 1 not in [j for subarray in subarrays for j in range(subarray[0], subarray[1] + 1)]:
            array[i] = mex
            mex += 1

    return array


n, m = map(int, input().split())
array = get_optimal_array(n, m)
print(array)

