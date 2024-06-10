
def can_start_dance(p):
    n = len(p)
    if n == 1:
        return True
    if n == 2:
        return p[0] == p[1]
    if p[0] != 1:
        return False
    for i in range(1, n-1):
        if p[i] != i+1:
            return False
    return p[n-1] == n

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES") if can_start_dance(p) else print("NO")

if __name__ == '__main__':
    main()

