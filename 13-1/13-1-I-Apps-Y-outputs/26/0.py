
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

def get_min_distance(x1, x2, v1, v2):
    if v1 == v2:
        return abs(x1 - x2)
    
    if v1 == 0 or v2 == 0:
        return abs(x1 - x2)
    
    if v1 > 0 and v2 > 0:
        if x1 < x2:
            return (x2 - x1) / (v1 - v2)
        else:
            return (x1 - x2) / (v1 - v2)
    
    if v1 < 0 and v2 < 0:
        if x1 > x2:
            return (x1 - x2) / (v1 - v2)
        else:
            return (x2 - x1) / (v1 - v2)
    
    if v1 > 0 and v2 < 0:
        if x1 < x2:
            return (x1 - x2) / (v1 + v2)
        else:
            return (x2 - x1) / (v1 + v2)
    
    if v1 < 0 and v2 > 0:
        if x1 > x2:
            return (x1 - x2) / (v1 + v2)
        else:
            return (x2 - x1) / (v1 + v2)

sum_min_distance = 0
for i in range(n):
    for j in range(i+1, n):
        sum_min_distance += get_min_distance(x[i], x[j], v[i], v[j])

print(sum_min_distance)

