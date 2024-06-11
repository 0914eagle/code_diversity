def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            if i == 0:
                arr[i] = arr[i] + arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]
                arr[i] = arr[i] - arr[i+1]
                arr[i+1] = arr[i] - arr[i+1]
                arr[i] = arr[i] + arr[i+1]