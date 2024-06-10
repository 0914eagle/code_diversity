
def is_sorted(p):
    return sorted(p) == p

def can_sort_permutation(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                if is_sorted(p):
                    return "YES"
                p[i], p[j] = p[j], p[i]
    return "NO"

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(can_sort_permutation(p))

if __name__ == '__main__':
    main()

