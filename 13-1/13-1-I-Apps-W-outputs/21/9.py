
def is_stack_sortable(arr):
    s = []
    b = []
    for i in range(len(arr)):
        if arr[i] != i+1:
            s.append(arr[i])
        else:
            b.append(arr[i])
    while s:
        top = s.pop()
        b.append(top)
    return b == list(range(1, len(arr)+1))

def restore_permutation(n, k, arr):
    if k == n:
        return arr
    if is_stack_sortable(arr):
        return arr
    for i in range(k, n):
        if arr[i] != i+1:
            break
    else:
        return -1
    for j in range(i+1, n):
        if arr[j] == i+1:
            break
    arr[i], arr[j] = arr[j], arr[i]
    return restore_permutation(n, k, arr)

