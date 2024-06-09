
import math

def get_min_angle(vectors):
    min_angle = math.pi
    min_angle_indices = []
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            angle = get_angle(vectors[i], vectors[j])
            if angle < min_angle:
                min_angle = angle
                min_angle_indices = [i, j]
    return min_angle_indices

def get_angle(v1, v2):
    dot_product = v1[0]*v2[0] + v1[1]*v2[1]
    magnitude1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magnitude2 = math.sqrt(v2[0]**2 + v2[1]**2)
    angle = math.acos(dot_product/(magnitude1*magnitude2))
    return angle

n = int(input())
vectors = []
for i in range(n):
    x, y = map(int, input().split())
    vectors.append([x, y])

indices = get_min_angle(vectors)
print(indices[0] + 1, indices[1] + 1)

