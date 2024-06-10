
def can_start_round_dance(p):
    n = len(p)
    if n == 1:
        return True
    if n == 2:
        return p[0] == p[1]
    if n == 3:
        return p[0] == p[1] and p[1] == p[2]
    if p[0] == p[n-1] and p[1] == p[2]:
        return True
    return False

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        if can_start_round_dance(p):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

