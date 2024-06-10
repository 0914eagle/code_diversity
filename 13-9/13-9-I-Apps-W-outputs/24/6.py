
def get_possible_resolutions(a, b, x, y):
    possible_resolutions = []
    for w in range(1, a+1):
        for h in range(1, b+1):
            if w/h == x/y and w <= a and h <= b:
                possible_resolutions.append((w, h))
    return possible_resolutions

def count_possible_resolutions(a, b, x, y):
    return len(get_possible_resolutions(a, b, x, y))

def main():
    a, b, x, y = map(int, input().split())
    print(count_possible_resolutions(a, b, x, y))

if __name__ == '__main__':
    main()

