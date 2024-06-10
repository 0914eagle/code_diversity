
def get_aspect_ratio(w, h, x, y):
    return w / h == x / y

def get_screen_resolution(a, b, x, y):
    count = 0
    for w in range(1, a + 1):
        for h in range(1, b + 1):
            if get_aspect_ratio(w, h, x, y) and w <= a and h <= b:
                count += 1
    return count

def main():
    a, b, x, y = map(int, input().split())
    print(get_screen_resolution(a, b, x, y))

if __name__ == '__main__':
    main()

