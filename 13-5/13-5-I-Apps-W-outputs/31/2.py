
def solve(n, m, cities, towers):
    # Sort the cities and towers in non-decreasing order
    cities = sorted(cities)
    towers = sorted(towers)
    
    # Initialize the minimum distance as 0
    min_dist = 0
    
    # Iterate through the cities and find the closest tower
    for i in range(n):
        # Find the closest tower to the current city
        closest_tower = binary_search(towers, cities[i])
        
        # If the closest tower is not found, return -1
        if closest_tower == -1:
            return -1
        
        # Update the minimum distance if necessary
        min_dist = max(min_dist, abs(cities[i] - towers[closest_tower]))
    
    return min_dist

# Binary search function to find the closest tower to a city
def binary_search(towers, city):
    left = 0
    right = len(towers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if towers[mid] == city:
            return mid
        elif towers[mid] < city:
            left = mid + 1
        else:
            right = mid - 1
    
    # If the tower is not found, return -1
    if left > right:
        return -1
    
    # If the tower is found, return its index
    return left

