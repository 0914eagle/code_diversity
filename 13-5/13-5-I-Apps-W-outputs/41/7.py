
def get_min_distance(x1, x2, x3):
    return abs(x1 - x2) + abs(x2 - x3) + abs(x3 - x1)

def main():
    x1, x2, x3 = map(int, input().split())
    print(get_min_distance(x1, x2, x3))

if __name__ == '__main__':
    main()

