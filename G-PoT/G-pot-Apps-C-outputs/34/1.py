
import math

def distance(hill1, hill2):
    return math.sqrt((hill1[0] - hill2[0])**2 + (hill1[1] - hill2[1])**2 + (hill1[2] - hill2[2])**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    total_length = 0
    for town in towns:
        min_length = float('inf')
        for spring in springs:
            length = distance(hills[town-1], hills[spring-1])
            if length < min_length:
                min_length = length
        total_length += min_length
    if total_length <= q:
        return total_length
    else:
        return "IMPOSSIBLE"

# Read input
n, s, t, q = map(int, input().split())
hills = []
for _ in range(n):
    hills.append(list(map(int, input().split())))
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the result
result = find_min_aqueduct_length(n, s, t, q, hills, springs, towns)
print(result)
