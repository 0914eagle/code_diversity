
def get_mex(arr):
    arr = sorted(arr)
    mex = 0
    for i in range(len(arr)):
        if arr[i] != mex:
            return mex
        mex += 1
    return mex + 1


def solve(queries, x):
    arr = []
    result = []
    for query in queries:
        arr.append(query)
        result.append(get_mex(arr))
    return result

