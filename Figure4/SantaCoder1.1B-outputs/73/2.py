def smallest_change(arr):
    
    # Write your code here
    n = len(arr)
    if n == 1:
        return 0
    elif n == 2:
        return 1 if arr[0] < arr[1] else 0
    else:
        for i in range(n - 2):
            if arr[i] > arr[i + 1]:
                return 1
        return 0


