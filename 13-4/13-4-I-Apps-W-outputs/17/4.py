
def solve(n, m, cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the closest tower
    for i in range(n):
        # Find the index of the closest tower to the current city
        tower_index = binary_search(towers, cities[i])
        
        # If the closest tower is not found, return -1
        if tower_index == -1:
            return -1
        
        # Update the minimum distance if necessary
        if cities[i] - towers[tower_index] > min_dist:
            min_dist = cities[i] - towers[tower_index]
    
    return min_dist

# Binary search function to find the closest tower to a city
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

