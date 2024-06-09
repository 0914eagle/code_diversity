
import math

def num_integer_pairs(points):
    num_pairs = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = math.sqrt(sum((points[i] - points[j])**2))
            if distance.is_integer():
                num_pairs += 1
    return num_pairs

points = []
for _ in range(int(input())):
    points.append(list(map(int, input().split())))

print(num_integer_pairs(points))
