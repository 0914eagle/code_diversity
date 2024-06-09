
def get_average_path_length(towns):
    # Calculate the distance between each pair of towns
    distances = []
    for i in range(len(towns)):
        for j in range(i+1, len(towns)):
            distance = ((towns[i][0]-towns[j][0])**2 + (towns[i][1]-towns[j][1])**2)**0.5
            distances.append(distance)
    
    # Calculate the average distance
    average_distance = sum(distances) / len(distances)
    
    return average_distance

