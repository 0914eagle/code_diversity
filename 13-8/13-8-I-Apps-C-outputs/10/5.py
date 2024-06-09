
def get_min_mex(subarrays):
    mex = 0
    for subarray in subarrays:
        mex = max(mex, *subarray) + 1
    return mex


def get_optimal_array(n, m):
    subarrays = []
    for _ in range(m):
        l, r = map(int, input().split())
        subarrays.append(list(range(l, r + 1)))

    mex = get_min_mex(subarrays)
    array = [mex] * n
    for subarray in subarrays:
        for i in subarray:
            array[i] = 0

    return array


n, m = map(int, input().split())
array = get_optimal_array(n, m)
print(array)

