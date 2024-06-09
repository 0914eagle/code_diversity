
def can_sort_permutation(p):
    n = len(p)
    for i in range(n):
        if p[i] != i + 1:
            j = p[i] - 1
            if j >= 0 and p[j] != i + 1:
                return "NO"
    return "YES"

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    print(can_sort_permutation(p))

