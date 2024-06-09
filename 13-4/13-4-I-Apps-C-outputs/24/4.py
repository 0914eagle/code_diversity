
def f1(h1, a1, x1, y1, h2, a2, x2, y2, m):
    # Initialize variables
    t = 0
    hx = h1
    ha = h2

    # Loop until Xaniar reaches a1 and Abol reaches a2
    while hx != a1 or ha != a2:
        # Update heights
        hx = (x1 * hx + y1) % m
        ha = (x2 * ha + y2) % m
        t += 1

    # Return minimum time
    return t

def f2(h1, a1, x1, y1, h2, a2, x2, y2, m):
    # Initialize variables
    t = 0
    hx = h1
    ha = h2

    # Loop until Xaniar reaches a1 and Abol reaches a2
    while hx != a1 or ha != a2:
        # Update heights
        hx = (x1 * hx + y1) % m
        ha = (x2 * ha + y2) % m
        t += 1

        # Check if heights are equal
        if hx == ha:
            return -1

    # Return minimum time
    return t

if __name__ == '__main__':
    h1, a1, x1, y1, h2, a2, x2, y2, m = map(int, input().split())
    print(f1(h1, a1, x1, y1, h2, a2, x2, y2, m))
    print(f2(h1, a1, x1, y1, h2, a2, x2, y2, m))

