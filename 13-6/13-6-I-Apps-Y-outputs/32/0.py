
def get_intersection(l1, r1, l2, r2):
    if l1 <= l2:
        return l2
    elif l2 <= r1:
        return r1
    else:
        return -1

def get_answer(l1, r1, l2, r2):
    intersection = get_intersection(l1, r1, l2, r2)
    if intersection != -1:
        return intersection, intersection + 1
    else:
        return l1, l2

def main():
    q = int(input())
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        a, b = get_answer(l1, r1, l2, r2)
        print(a, b)

if __name__ == '__main__':
    main()

