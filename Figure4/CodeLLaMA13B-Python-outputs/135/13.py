def can_arrange(arr):
    
    # Your code here
    # if len(arr) == 0:
    #     return -1
    # for i in range(len(arr) - 1):
    #     if arr[i] >= arr[i + 1]:
    #         return i
    # return -1
    # return max(i for i in range(len(arr) - 1) if arr[i] >= arr[i + 1])
    # return max(range(len(arr) - 1), key=lambda i: arr[i] >= arr[i + 1])
    # return max(range(len(arr) - 1), key=lambda i: arr[i] >= arr[i + 1]) if any(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)) else -1
    # return max(range(len(arr) - 1), key=lambda i: arr[i] >= arr[i + 1]) if any(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)) else -1
    return max(range(len(arr) - 1), key=lambda i: arr[i] >= arr[i + 1]) if any(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)) else -1
