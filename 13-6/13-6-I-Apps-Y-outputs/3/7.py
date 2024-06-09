
def get_minimum_heaters(n, r, arr):
    # Sort the array and find the leftmost and rightmost warm positions
    arr.sort()
    leftmost_warm = 0
    rightmost_warm = 0
    for i in range(n):
        if arr[i] == 1:
            leftmost_warm = i
            break
    for i in range(n-1, -1, -1):
        if arr[i] == 1:
            rightmost_warm = i
            break
    
    # Initialize the number of heaters needed to warm up the whole house
    num_heaters = 0
    
    # Iterate through the array and check if each element is warmed up by at least one heater
    for i in range(n):
        # If the element is not warmed up by any heater, increment the number of heaters needed
        if arr[i] == 0:
            num_heaters += 1
        # If the element is warmed up by a heater, check if it is within the range of the heater
        else:
            # If the element is within the range of the heater, do nothing
            if i >= leftmost_warm - r + 1 and i <= rightmost_warm + r - 1:
                pass
            # If the element is not within the range of the heater, increment the number of heaters needed
            else:
                num_heaters += 1
    
    return num_heaters

