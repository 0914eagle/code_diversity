
def can_sort_permutation(p):
    n = len(p)
    # Check if p is a permutation of {1, 2, ..., n}
    if set(p) != set(range(1, n+1)):
        return "NO"
    
    # Check if p can be sorted in ascending order
    sorted_p = sorted(p)
    if p == sorted_p:
        return "YES"
    
    # Check if p can be sorted in ascending order by swapping two elements
    for i in range(n-1):
        for j in range(i+1, n):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                if p == sorted_p:
                    return "YES"
                p[i], p[j] = p[j], p[i]
    
    return "NO"

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    print(can_sort_permutation(p))

