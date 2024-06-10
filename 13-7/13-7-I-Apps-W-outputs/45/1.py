
def get_weight(h, w, u1, d1, u2, d2):
    while h > 0:
        w += h
        if h == d1 or h == d2:
            w -= u1 if h == d1 else u2
            if w < 0:
                w = 0
        h -= 1
    return w

def main():
    h, w = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    print(get_weight(h, w, u1, d1, u2, d2))

if __name__ == '__main__':
    main()

