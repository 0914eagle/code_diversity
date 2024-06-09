
import math

def get_closest_distance(contour_lines):
    # Calculate the distance from the surface to the target for each contour line
    distances = []
    for contour in contour_lines:
        distance = 0
        for i in range(len(contour) - 1):
            x1, y1 = contour[i]
            x2, y2 = contour[i + 1]
            distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distances.append(distance)
    
    # Return the minimum distance
    return min(distances)

