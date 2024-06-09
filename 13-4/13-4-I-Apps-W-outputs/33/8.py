
def count_subpermutations(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if len(set(arr[i:j+1])) == j - i + 1:
                count += 1
    return count

