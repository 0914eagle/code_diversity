
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
    for query in queries:
        arr.append(query)
        arr = sorted(arr)
        for i in range(len(arr)):
            if arr[i] != i:
                break
        else:
            return i + 1
        arr[i] += x
    return get_mex(arr)

