
import math

def get_largest_piece(n, h, v):
    # Calculate the area of each piece
    area_1 = (n - h) * (n - v)
    area_2 = h * (n - v)
    area_3 = (n - h) * v
    area_4 = h * v

    # Calculate the volume of each piece
    volume_1 = area_1 * 4
    volume_2 = area_2 * 4
    volume_3 = area_3 * 4
    volume_4 = area_4 * 4

    # Find the largest piece
    largest_piece = max(volume_1, volume_2, volume_3, volume_4)

    return largest_piece

n, h, v = map(int, input().split())
print(get_largest_piece(n, h, v))

