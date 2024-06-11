def move_one_ball(arr):
    
    # Your code here
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            if i == 0:
                arr[i] = arr[i] + arr[i+1]
                arr[i+1] = 0
            elif i == len(arr)-1:
                arr[i] = arr[i] + arr[i-1]
                arr[i-1] = 0
            else:
                arr[i] = arr[i] + arr[i+1]
                arr[i+1] = arr[i] + arr[i-1]
                arr[i-1] = 0
        return True

print(move_one_ball([3, 4, 5, 1, 2]))
print(move_one_ball([3, 5, 4, 1, 2]))
print(move_one_ball([3, 4, 5, 1, 2, 6]))
print(move_one_ball([3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 7