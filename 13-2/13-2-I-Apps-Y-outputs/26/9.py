
def is_sorted(p):
    return sorted(p) == p

def can_sort_permutation(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                return True
    return False

def solve(p):
    if is_sorted(p):
        return "YES"
    if can_sort_permutation(p):
        return "YES"
    return "NO"

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(p))

