
def can_start_round_dance(p):
    n = len(p)
    for i in range(n):
        if p[i] != i + 1 and p[(i + 1) % n] != p[i] + 1:
            return "NO"
    return "YES"

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(can_start_round_dance(p))

if __name__ == '__main__':
    main()

