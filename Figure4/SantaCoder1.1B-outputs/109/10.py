def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            if i == 0:
                arr[i] = arr[i] + arr[i + 1]
            elif i == len(arr) - 1:
                arr[i] = arr[i] + arr[i - 1]
            else:
                arr[i] = arr[i] + arr[i - 1] + arr[i + 1]
        return arr[0] > arr[-1]


if __name__ == "__main__":
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one_ball([3, 5, 4, 1, 2]))
    print(move_one_ball([3, 4, 5, 1, 2, 6]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 9]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 9, 10]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 11]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 11, 12]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 