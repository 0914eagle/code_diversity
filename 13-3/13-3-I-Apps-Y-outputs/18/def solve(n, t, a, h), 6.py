
def solve(n, t, a, h):
    # Calculate the average temperature at each place
    avg_temp = [t - x * 0.006 for x in h]
    
    # Find the index of the place with the closest average temperature to A
    closest_index = avg_temp.index(min(avg_temp, key=lambda x: abs(x - a)))
    
    return closest_index + 1

