
def ultra_quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return 0
    else:
        left = []
        right = []
        pivot = arr[0]
        for i in range(1, n):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return ultra_quick_sort(left) + ultra_quick_sort(right) + 1

