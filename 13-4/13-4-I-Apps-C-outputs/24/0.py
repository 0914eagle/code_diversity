
def f1(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize variables
    t = 0
    hx = h1
    ha = h2
    while hx != a1 or ha != a2:
        # Update heights
        hx = (x1 * hx + y1) % m
        ha = (x2 * ha + y2) % m
        t += 1
    return t

def f2(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize variables
    t = 0
    hx = h1
    ha = h2
    while hx != a1 or ha != a2:
        # Update heights
        hx = (x1 * hx + y1) % m
        ha = (x2 * ha + y2) % m
        t += 1
    return t

if __name__ == '__main__':
    m = int(input())
    h1, a1 = map(int, input().split())
    x1, y1 = map(int, input().split())
    h2, a2 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(f1(m, h1, a1, x1, y1, h2, a2, x2, y2))

