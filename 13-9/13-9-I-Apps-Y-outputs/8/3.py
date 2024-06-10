
def can_start_round_dance(permutation):
    n = len(permutation)
    for i in range(n):
        if permutation[i] != i + 1:
            return False
    return True

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        permutation = list(map(int, input().split()))
        if can_start_round_dance(permutation):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

