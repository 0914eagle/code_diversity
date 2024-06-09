
def get_closest_place(N, T, A, H):
    # Calculate the average temperature at each place
    average_temperatures = [T - x * 0.006 for x in H]
    
    # Find the index of the place with the closest average temperature to A
    closest_index = 0
    for i in range(1, N):
        if abs(average_temperatures[i] - A) < abs(average_temperatures[closest_index] - A):
            closest_index = i
    
    return closest_index + 1

