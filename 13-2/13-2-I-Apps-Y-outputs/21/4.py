
import math

def get_volume(n, h, v):
    # Calculate the area of the largest piece of cake
    area = (n - h) * (n - v)
    
    # Calculate the volume of the largest piece of cake
    volume = area * 4
    
    return volume

n, h, v = map(int, input().split())
print(get_volume(n, h, v))

