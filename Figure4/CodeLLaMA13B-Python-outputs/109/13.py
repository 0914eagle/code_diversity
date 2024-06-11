def move_one_ball(arr):
    
    if not arr:
        return True
    if arr == sorted(arr):
        return True
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            return True
    return False


if __name__ == "__main__":
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one_ball([