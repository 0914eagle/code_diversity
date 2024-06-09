
def ultra_quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return 0
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return 1 + ultra_quick_sort(left) + ultra_quick_sort(right)

