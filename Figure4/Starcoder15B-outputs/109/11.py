def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))
print(move_one_ball([3, 5,