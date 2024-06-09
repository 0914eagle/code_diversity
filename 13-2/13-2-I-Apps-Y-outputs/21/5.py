
import math

def get_volume(n, h, v):
    # Calculate the volume of the largest piece of cake
    volume = (n - h) * (n - v) * 4
    return volume

n, h, v = map(int, input().split())
print(get_volume(n, h, v))

