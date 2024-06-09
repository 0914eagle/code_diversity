
import math

def get_distance(t):
    
    agneta_x = math.sin(t)
    agneta_y = math.cos(t)
    beata_x = math.sin(t + 1)
    beata_y = math.cos(t + 1)
    return math.sqrt((agneta_x - beata_x) ** 2 + (agneta_y - beata_y) ** 2)

def find_min_distance(w):
    
    min_distance = float('inf')
    for t in range(1000):
        distance = get_distance(t * w)
        if distance < min_distance:
            min_distance = distance
    return min_distance

if __name__ == '__main__':
    w = float(input())
    print(find_min_distance(w))

