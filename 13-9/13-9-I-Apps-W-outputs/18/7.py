
def check_arrays(arr1, arr2, k, m):
    if len(arr1) < k or len(arr2) < m:
        return "NO"
    for i in range(k):
        for j in range(m):
            if arr1[i] >= arr2[j]:
                return "NO"
    return "YES"

