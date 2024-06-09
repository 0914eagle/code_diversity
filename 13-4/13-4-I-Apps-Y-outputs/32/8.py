
def get_mex(arr):
    arr = set(arr)
    for i in range(len(arr)):
        if i not in arr:
            return i
    return len(arr) + 1


def solve(queries, x):
    arr = []
    result = []
    for query in queries:
        arr.append(query)
        result.append(get_mex(arr))
    return result

