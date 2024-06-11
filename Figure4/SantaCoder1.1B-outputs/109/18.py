def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        if i == 0:
            arr[i] = arr[i] + 1
        elif arr[i] > arr[i - 1]:
            arr[i] = arr[i] + 1
    return True if arr[0] == len(arr) else False


if __name__ == "__main__":
    print(move_one_