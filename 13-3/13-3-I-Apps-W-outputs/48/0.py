
def is_ladder(arr):
    # Check if the array is non-decreasing
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    
    # Check if the array is non-increasing
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            return False
    
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    l, r = map(int, input().split())
    subarr = arr[l-1:r]
    if is_ladder(subarr):
        print("Yes")
    else:
        print("No")

