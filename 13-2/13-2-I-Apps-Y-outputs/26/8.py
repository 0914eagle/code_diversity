
def can_sort_permutation(p):
    n = len(p)
    if n == 2:
        return True
    if n == 3:
        if p[0] < p[1] and p[1] < p[2]:
            return True
        else:
            return False
    if n == 4:
        if p[0] < p[1] and p[2] < p[3]:
            return True
        else:
            return False
    if n == 5:
        if p[0] < p[1] and p[2] < p[3] and p[4] < p[5]:
            return True
        else:
            return False
    return False

def main():
    n = int(input())
    p = list(map(int, input().split()))
    if can_sort_permutation(p):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

