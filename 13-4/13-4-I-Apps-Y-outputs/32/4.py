
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
        for i in range(len(arr)):
            if arr[i] < 0:
                arr[i] = 0
        print(get_mex(arr))

q, x = map(int, input().split())
queries = [int(input()) for _ in range(q)]
solve(q, x, queries)

