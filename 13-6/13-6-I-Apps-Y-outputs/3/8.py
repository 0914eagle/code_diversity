
def get_min_heaters(n, r, arr):
    # Sort the array and find the maximum range that can be warmed up
    arr.sort()
    max_range = arr[-1] - arr[0]

    # Initialize the number of heaters needed to warm up the whole house
    num_heaters = 0

    # Iterate through the array and check if the current element is within the range of the heater
    for i in range(n):
        if arr[i] + r - 1 >= max_range:
            break
        num_heaters += 1

    return num_heaters

