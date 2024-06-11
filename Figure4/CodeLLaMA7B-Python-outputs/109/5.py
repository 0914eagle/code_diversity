def move_one_ball(arr):
    
    if len(arr)==0:
        return True
    if arr[-1]>arr[0]:
        return False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


if __name__=="__main__":
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one