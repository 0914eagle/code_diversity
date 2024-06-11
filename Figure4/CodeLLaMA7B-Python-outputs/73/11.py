def smallest_change(arr):
    
    # Your code here
    # 1. find the middle of the array
    # 2. check if the middle is odd or even
    # 3. if odd, check if the middle is the same as the first element
    # 4. if even, check if the middle is the same as the first and last element
    # 5. if not, check if the middle is the same as the first or last element
    # 6. if not, return the middle element
    # 7. if it is, check if the middle is the same as the first and last element
    # 8. if not, return the middle element
    # 9. if it is, return 0

    # 1. find the middle of the array
    middle = len(arr) // 2

    # 2. check if the middle is odd or even
    if len(arr) % 2 == 0:
        # 3. if odd, check if the middle is the same as the first element
        if arr[middle] != arr[0]:
            # 4. if even, check if the middle is the same as the first and last element
            if arr[middle] != arr[len(arr) - 1]:
                # 5. if not, check if the middle is the same as the first or last element
                if arr[middle] != arr[0] and arr[middle] != arr[len(arr) - 1]:
                    # 6. if not, return the middle element
                    return arr[middle]
                # 7. if it is, check if the middle is the same as the first and last element
                if arr[middle] == arr[0] and arr[middle] == arr[len(arr) - 1]:
                    # 8. if not, return the middle element
                    return arr[middle]
            # 9. if it is, return 0
            return 0
    else:
        # 3. if odd, check if the middle is the same as the first element
        if arr[middle] != arr[0]:
            # 4. if even, check if the middle is the same as the first and last element
            if arr[middle] !=