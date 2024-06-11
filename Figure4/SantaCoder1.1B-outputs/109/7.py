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
                arr[i] = arr[i] + arr[i-1]
                arr[i-1] = 0
        return True

if __name__ == "__main__":
    arr = [3, 4, 5, 1, 2]
    print(move_one_ball(arr))