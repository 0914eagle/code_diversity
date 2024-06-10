
def get_triangle_area(a, b, c):
    perimeter = a + b + c
    semiperimeter = perimeter / 2
    area = semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)
    return area

def get_min_minutes(a, b, c):
    area = get_triangle_area(a, b, c)
    if area > 0:
        return 0
    else:
        max_length = max(a, b, c)
        min_length = min(a, b, c)
        mid_length = a + b + c - max_length - min_length
        return max_length - min_length + mid_length - 1

def main():
    a, b, c = map(int, input().split())
    print(get_min_minutes(a, b, c))

if __name__ == '__main__':
    main()

