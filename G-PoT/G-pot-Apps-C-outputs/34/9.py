
import math

def distance(hill1, hill2):
    return math.sqrt((hill1[0] - hill2[0])**2 + (hill1[1] - hill2[1])**2 + (hill1[2] - hill2[2])**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    min_length = float('inf')
    
    for spring_hill in springs:
        for town_hill in towns:
            length = distance(hills[spring_hill-1], hills[town_hill-1])
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
    hills.append(list(map(int, input().split())))
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the result
result = find_min_aqueduct_length(n, s, t, q, hills, springs, towns)
print(result)
