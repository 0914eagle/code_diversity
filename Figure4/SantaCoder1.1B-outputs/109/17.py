def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        if i == 0:
            arr[i] = arr[i] + 1
            continue
        if arr[i] > arr[i - 1]:
            arr[i] = arr[i] + 1
        else:
            arr[i] = arr[i - 1] + 1
    return arr == sorted(arr)


if __name__ == '__main__':
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one_ball([3, 5, 4, 1,