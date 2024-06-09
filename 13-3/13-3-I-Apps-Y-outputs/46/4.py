
def is_triangle(a, b, c):
    return a**2 + b**2 > c**2

def count_triangles(sticks):
    count = 0
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[i] != sticks[k]:
                    if is_triangle(sticks[i], sticks[j], sticks[k]):
                        count += 1
    return count

n = int(input())
sticks = list(map(int, input().split()))
print(count_triangles(sticks))

