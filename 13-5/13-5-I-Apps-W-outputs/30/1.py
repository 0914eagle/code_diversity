
import math

def get_distance(t):
    agneta_x = math.cos(t)
    agneta_y = math.sin(t)
    beata_x = math.cos(t + math.pi)
    beata_y = math.sin(t + math.pi)
    return math.sqrt((agneta_x - beata_x)**2 + (agneta_y - beata_y)**2)

def find_min_distance(w):
    min_distance = float('inf')
    for t in range(0, 1001):
        distance = get_distance(t)
        if distance < min_distance:
            min_distance = distance
    return min_distance

if __name__ == '__main__':
    w = float(input())
    print(find_min_distance(w))

