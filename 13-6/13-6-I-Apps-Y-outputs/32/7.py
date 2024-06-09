
def find_intersection(l1, r1, l2, r2):
    if l1 <= l2:
        return l1, l2
    elif l1 <= r2:
        return l1, r2
    elif l2 <= r1:
        return l2, r1
    else:
        return None

def find_intersection_points(l1, r1, l2, r2):
    intersection = find_intersection(l1, r1, l2, r2)
    if intersection:
        a, b = intersection
        if a != b:
            return a, b
    return None

def main():
    q = int(input())
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        intersection = find_intersection_points(l1, r1, l2, r2)
        if intersection:
            a, b = intersection
            print(a, b)
        else:
            print(-1)

if __name__ == '__main__':
    main()

