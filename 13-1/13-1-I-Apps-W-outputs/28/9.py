
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
            break
    else:
        return [-1]
    temp = arr[i]
    arr[i] = arr[k-1]
    arr[k-1] = temp
    return restore_permutation(arr, k-1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if is_stack_sortable(arr):
        print(*arr)
    else:
        print(*restore_permutation(arr, k))

