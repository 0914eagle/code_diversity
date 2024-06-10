
def can_sort(p):
    # Check if p is a permutation of {1, 2, ..., N}
    if len(p) != len(set(p)):
        return "NO"
    
    # Check if p can be sorted in ascending order
    sorted_p = sorted(p)
    if p == sorted_p:
        return "YES"
    
    # Check if p can be sorted in ascending order after one swap
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                if p == sorted_p:
                    return "YES"
                p[i], p[j] = p[j], p[i]
    
    # If p cannot be sorted in ascending order, return "NO"
    return "NO"

def main():
    N = int(input())
    p = list(map(int, input().split()))
    print(can_sort(p))

if __name__ == '__main__':
    main()

