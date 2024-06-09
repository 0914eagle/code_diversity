
import math

def average_path_length(towns):
    # Calculate the distance between each pair of towns
    distances = []
    for i in range(len(towns)):
        for j in range(i+1, len(towns)):
            distance = math.sqrt((towns[i][0] - towns[j][0])**2 + (towns[i][1] - towns[j][1])**2)
            distances.append(distance)
    
    # Calculate the average length of all paths
    total_distance = sum(distances)
    num_paths = len(distances)
    average_length = total_distance / num_paths
    
    return average_length

