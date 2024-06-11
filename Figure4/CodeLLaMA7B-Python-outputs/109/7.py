def move_one_ball(arr):
    
    if len(arr) == 0:
        return True

    if len(arr) == 1:
        return True

    if len(arr) == 2:
        if arr[0] <= arr[1]:
            return True
        else:
            return False

    if arr[0] <= arr[1]:
        return move_one_ball(arr[1:])
    else:
        return move_one_ball(arr[1:]) and move_one_ball(arr[:-1])


if __name__ == "__main__":
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one_ball([3, 5, 4, 1, 2]))
