
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

def restore_permutation(arr, k):
    if k == 0:
        return [-1]
    if k == len(arr):
        return arr
    for i in range(k):
        if arr[i] != i+1:
            break
    else:
        return arr
    for i in range(k, len(arr)):
        if arr[i] == i+1:
            continue
        for j in range(i+1, len(arr)):
            if arr[j] == i+1:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return restore_permutation(arr, k)

def solve(n, k, arr):
    if k == 0:
        return [-1]
    if k == len(arr):
        return arr
    for i in range(k):
        if arr[i] != i+1:
            break
    else:
        return arr
    for i in range(k, len(arr)):
        if arr[i] == i+1:
            continue
        for j in range(i+1, len(arr)):
            if arr[j] == i+1:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return restore_permutation(arr, k)

