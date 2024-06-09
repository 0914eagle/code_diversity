
a, b, h, w, n = map(int, input().split())
extensions = list(map(int, input().split()))

def can_place_rectangle(a, b, h, w):
    return (a <= h and b <= w) or (a <= w and b <= h)

if can_place_rectangle(a, b, h, w):
    print(0)
else:
    min_extensions = float('inf')
    for extension in extensions:
        new_h = h * extension
        new_w = w
        if can_place_rectangle(a, b, new_h, new_w):
            min_extensions = min(min_extensions, 1)
        
        new_h = h
        new_w = w * extension
        if can_place_rectangle(a, b, new_h, new_w):
            min_extensions = min(min_extensions, 1)
    
    if min_extensions == float('inf'):
        print(-1)
    else:
        print(min_extensions)
