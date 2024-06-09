
def get_intersection(l1, r1, l2, r2):
    if l1 <= l2:
        return l2, r2
    else:
        return l1, r1

def get_intersection_points(l1, r1, l2, r2):
    intersection = get_intersection(l1, r1, l2, r2)
    a = intersection[0]
    b = intersection[1]
    return a, b

def main():
    q = int(input())
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        a, b = get_intersection_points(l1, r1, l2, r2)
        print(a, b)

if __name__ == '__main__':
    main()

