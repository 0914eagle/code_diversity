
def can_start_round_dance(n, p):
    # Check if the permutation is a circle
    if p[0] != 1:
        return "NO"
    # Check if the permutation is a circle
    if p[-1] != n:
        return "NO"
    # Check if the permutation is a circle
    for i in range(1, n):
        if p[i] != i + 1:
            return "NO"
    return "YES"

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(can_start_round_dance(n, p))

if __name__ == '__main__':
    main()

