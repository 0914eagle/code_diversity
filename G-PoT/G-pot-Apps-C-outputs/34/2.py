
import math

def distance(hill1, hill2):
    return math.sqrt((hill1[0] - hill2[0])**2 + (hill1[1] - hill2[1])**2 + (hill1[2] - hill2[2])**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    min_length = float('inf')
    
    for i in range(s):
        for j in range(t):
            length = distance(hills[springs[i]-1], hills[towns[j]-1])
            if length <= q:
                min_length = min(min_length, length)
    
    if min_length == float('inf'):
        return "IMPOSSIBLE"
    else:
        return round(min_length, 6)

# Input parsing
n, s, t, q = map(int, input().split())
hills = []
for _ in range(n):
    x, y, h = map(int, input().split())
    hills.append((x, y, h))
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and output the result
result = find_min_aqueduct_length(n, s, t, q, hills, springs, towns)
print(result)
