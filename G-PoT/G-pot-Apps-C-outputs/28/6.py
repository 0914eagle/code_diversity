
a, b, h, w, n = map(int, input().split())
extensions = list(map(int, input().split()))

def can_place(a, b, h, w):
    return (a <= h and b <= w) or (a <= w and b <= h)

if can_place(a, b, h, w):
    print(0)
else:
    min_extensions = float('inf')
    for ext in extensions:
        new_h = h * ext
        new_w = w * ext
        if can_place(a, b, new_h, new_w):
            min_extensions = min(min_extensions, 1)
        else:
            for ext2 in extensions:
                new_h2 = new_h * ext2
                new_w2 = new_w * ext2
                if can_place(a, b, new_h2, new_w2):
                    min_extensions = min(min_extensions, 2)
    if min_extensions == float('inf'):
        print(-1)
    else:
        print(min_extensions)
