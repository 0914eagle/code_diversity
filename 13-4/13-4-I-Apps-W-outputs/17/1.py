
def solve(n, m, cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the closest tower
    for i in range(n):
        # Find the closest tower to the current city
        tower_index = binary_search(towers, cities[i])
        
        # If the closest tower is not found, return -1
        if tower_index == -1:
            return -1
        
        # Update the minimum distance if necessary
        min_dist = max(min_dist, abs(cities[i] - towers[tower_index]))
    
    return min_dist

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

