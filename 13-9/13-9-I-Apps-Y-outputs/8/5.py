
def can_start_round_dance(n, p):
    # Check if the permutation is a circular permutation
    if len(set(p)) == n and len(p) == n:
        # Check if the permutation is a circular permutation
        if p[0] == 1 and p[-1] == n:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(can_start_round_dance(n, p))

if __name__ == '__main__':
    main()

