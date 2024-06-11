def move_one_ball(arr):
    
    if len(arr) == 0:
        return True
    else:
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

if __name__ == "__main__":
    arr = [3, 4, 5, 1, 2]
    print(move_one_ball(arr))
