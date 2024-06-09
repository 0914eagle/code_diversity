
import math

def distance(hill1, hill2):
    return math.sqrt((hill1[0] - hill2[0])**2 + (hill1[1] - hill2[1])**2 + (hill1[2] - hill2[2])**2)

def find_min_aqueduct_length(n, s, t, q, hills, springs, towns):
    min_length = float('inf')
    
    for spring_hill in springs:
        for town_hill in towns:
            if spring_hill != town_hill:
                aqueduct_lengths = []
                for i in range(n):
                    for j in range(n):
                        if i != j:
                            length = distance(hills[i], hills[j])
                            if length <= q:
                                aqueduct_lengths.append(length)
                
                total_length = sum(sorted(aqueduct_lengths)[:s+t-2])
                min_length = min(min_length, total_length)
    
    if min_length == float('inf'):
        return "IMPOSSIBLE"
    else:
        return round(min_length, 6)

# Input parsing
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Call the function and print the result
result = find_min_aqueduct_length(n, s, t, q, hills, springs, towns)
print(result)
