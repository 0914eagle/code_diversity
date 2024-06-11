def move_one_ball(arr):
    
    # Your code here
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        if arr[i] > arr[(i+1)%len(arr)]:
            return False
    return True

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))
print(move_