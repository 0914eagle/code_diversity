
def get_max_prettiness(a):
    
    a.sort(reverse=True)
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return a[0] + a[1]
    if len(a) == 3:
        return a[0] + a[1] + a[2]
    if len(a) == 4:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3])
    if len(a) == 5:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3], a[0] + a[3] + a[4])
    if len(a) == 6:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3], a[0] + a[3] + a[4], a[0] + a[4] + a[5])
    if len(a) == 7:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3], a[0] + a[3] + a[4], a[0] + a[4] + a[5], a[0] + a[5] + a[6])
    if len(a) == 8:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3], a[0] + a[3] + a[4], a[0] + a[4] + a[5], a[0] + a[5] + a[6], a[0] + a[6] + a[7])
    if len(a) == 9:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3], a[0] + a[3] + a[4], a[0] + a[4] + a[5], a[0] + a[5] + a[6], a[0] + a[6] + a[7], a[0] + a[7] + a[8])
    if len(a) == 10:
        return max(a[0] + a[1] + a[2], a[0] + a[2] + a[3], a[0] + a[3] + a[4], a[0] + a[4] + a[5], a[0] + a[5] + a[6], a[0] + a[6] + a[7], a[0] + a[7] + a[8], a[0] + a[8] + a[9])


def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_max_prettiness(a))


if __name__ == '__main__':
    main()

