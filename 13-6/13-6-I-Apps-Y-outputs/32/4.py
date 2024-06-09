
def get_intersection(l1, r1, l2, r2):
    if l1 <= l2:
        if r1 >= l2:
            return l2
        elif r1 >= r2:
            return r2
        else:
            return 0
    else:
        if l1 <= r2:
            return l1
        elif r1 >= r2:
            return r2
        else:
            return 0

def solve(l1, r1, l2, r2):
    intersection = get_intersection(l1, r1, l2, r2)
    if intersection != 0:
        return [intersection, intersection]
    else:
        if l1 <= l2:
            return [l1, r2]
        else:
            return [l2, r1]

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        print(*solve(l1, r1, l2, r2))

