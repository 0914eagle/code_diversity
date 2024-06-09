
import math

def get_average_path_length(coordinates):
    num_towns = len(coordinates)
    total_length = 0
    for i in range(num_towns):
        for j in range(i+1, num_towns):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            total_length += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return total_length / math.factorial(num_towns)

