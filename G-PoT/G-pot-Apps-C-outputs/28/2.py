
a, b, h, w, n = map(int, input().split())
extensions = list(map(int, input().split()))

def can_place_rectangle(a, b, h, w):
    return (a <= h and b <= w) or (a <= w and b <= h)

if can_place_rectangle(a, b, h, w):
    print(0)
else:
    min_extensions = float('inf')
    for i in range(1 << n):
        new_h, new_w = h, w
        for j in range(n):
            if i & (1 << j):
                new_h *= extensions[j]
            else:
                new_w *= extensions[j]
        
        if can_place_rectangle(a, b, new_h, new_w):
            min_extensions = min(min_extensions, bin(i).count('1'))
    
    if min_extensions == float('inf'):
        print(-1)
    else:
        print(min_extensions)
