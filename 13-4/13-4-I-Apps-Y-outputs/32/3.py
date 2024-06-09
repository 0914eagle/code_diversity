
def get_mex(arr):
    arr = sorted(arr)
    mex = 0
    for i in range(len(arr)):
        if arr[i] != mex:
            return mex
        mex += 1
    return mex + 1


def solve(q, x, queries):
    arr = []
    for query in queries:
        arr.append(query)
        get_mex(arr)
    return arr

