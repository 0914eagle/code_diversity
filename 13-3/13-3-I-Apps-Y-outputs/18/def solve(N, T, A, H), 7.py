
def solve(N, T, A, H):
    # Calculate the average temperature at each place
    avg_temp = [T - h * 0.006 for h in H]
    
    # Find the index of the place with the closest average temperature to A
    closest_index = avg_temp.index(min(avg_temp, key=lambda x: abs(x - A)))
    
    return closest_index + 1

