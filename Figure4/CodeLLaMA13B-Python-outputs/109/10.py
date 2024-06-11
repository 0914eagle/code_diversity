def move_one_ball(arr):
    
    if not arr:
        return True
    if len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False
    return move_one_ball(arr[1:])


if __name__ == "__main__":
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one_ball([3