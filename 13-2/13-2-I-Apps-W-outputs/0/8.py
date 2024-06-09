
import math

def get_star_area(n, r):
    # Calculate the area of a regular polygon
    area = (n * r ** 2) / (4 * math.tan(math.pi / n))
    return area

n, r = map(int, input().split())
print(get_star_area(n, r))

