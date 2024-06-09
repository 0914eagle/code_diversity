
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    min_length = float('inf')
    
    for i in range(s):
        for j in range(t):
            spring_hill = hills[springs[i]-1]
            town_hill = hills[towns[j]-1]
            length = distance(spring_hill[0], spring_hill[1], town_hill[0], town_hill[1]) + abs(spring_hill[2] - town_hill[2])
            min_length = min(min_length, length)
    
    if min_length <= q:
        return min_length
    else:
        return "IMPOSSIBLE"

# Read input
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the output
print(find_min_aqueduct_length(n, s, t, q, hills, springs, towns))
