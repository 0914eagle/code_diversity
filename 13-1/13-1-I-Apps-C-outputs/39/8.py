
def get_min_distance(adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles):
    # Calculate the distance from Adil and Bera to the recycling bin
    adil_distance = abs(adil_x - recycling_bin_x) + abs(adil_y - recycling_bin_y)
    bera_distance = abs(bera_x - recycling_bin_x) + abs(bera_y - recycling_bin_y)
    
    # Initialize the minimum distance to the maximum possible value
    min_distance = float('inf')
    
    # Iterate over all possible combinations of bottles that Adil and Bera can pick
    for i in range(len(bottles)):
        for j in range(i+1, len(bottles)):
            # Calculate the distance from Adil and Bera to the current combination of bottles
            adil_distance_to_bottles = abs(adil_x - bottles[i][0]) + abs(adil_y - bottles[i][1])
            bera_distance_to_bottles = abs(bera_x - bottles[j][0]) + abs(bera_y - bottles[j][1])
            
            # Calculate the total distance from Adil and Bera to the recycling bin
            total_distance = adil_distance_to_bottles + bera_distance_to_bottles + adil_distance + bera_distance
            
            # Update the minimum distance if necessary
            if total_distance < min_distance:
                min_distance = total_distance
    
    return min_distance

