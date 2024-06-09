
def find_place_to_build_palace(n, t, a, h):
    # Calculate the average temperature at each place
    average_temperatures = [t - x * 0.006 for x in h]
    
    # Find the place with the closest average temperature to A
    closest_place = 0
    for i in range(1, n):
        if abs(average_temperatures[i] - a) < abs(average_temperatures[closest_place] - a):
            closest_place = i
    
    return closest_place

