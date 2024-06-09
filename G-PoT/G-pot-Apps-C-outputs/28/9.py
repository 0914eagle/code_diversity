
a, b, h, w, n = map(int, input().split())
extensions = list(map(int, input().split()))

def can_place_rectangle(a, b, h, w):
    return (a <= h and b <= w) or (a <= w and b <= h)

if can_place_rectangle(a, b, h, w):
    print(0)
else:
    min_extensions = float('inf')
    for i in range(1 << n):
        current_h, current_w = h, w
        used_extensions = 0
        for j in range(n):
            if i & (1 << j):
                current_h *= extensions[j]
            else:
                current_w *= extensions[j]
            used_extensions += 1
            if can_place_rectangle(a, b, current_h, current_w):
                min_extensions = min(min_extensions, used_extensions)
    if min_extensions == float('inf'):
        print(-1)
    else:
        print(min_extensions)
