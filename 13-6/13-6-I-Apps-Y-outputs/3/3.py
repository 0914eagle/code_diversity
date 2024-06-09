
def get_min_heaters(n, r, arr):
    # Sort the array and find the maximum number of elements that can be warmed up by each heater
    arr.sort()
    max_elements = [0] * len(arr)
    for i in range(len(arr)):
        if i + r - 1 < len(arr):
            max_elements[i] = arr[i + r - 1] - arr[i] + 1
        else:
            max_elements[i] = arr[len(arr) - 1] - arr[i] + 1
    
    # Initialize the number of heaters needed to warm up the whole house as the maximum number of elements
    num_heaters = max(max_elements)
    
    # Iterate through the array and find the minimum number of heaters needed to warm up each element
    for i in range(len(arr)):
        num_heaters = min(num_heaters, max_elements[i])
    
    return num_heaters

