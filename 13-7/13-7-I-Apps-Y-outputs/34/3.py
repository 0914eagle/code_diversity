
def get_input():
    N = int(input())
    p = list(map(int, input().split()))
    return N, p

def is_sorted(p):
    return all(p[i] < p[i+1] for i in range(len(p)-1))

def can_sort(N, p):
    if is_sorted(p):
        return "YES"
    
    for i in range(N):
        for j in range(i+1, N):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                if is_sorted(p):
                    return "YES"
                p[i], p[j] = p[j], p[i]
    
    return "NO"

if __name__ == '__main__':
    N, p = get_input()
    print(can_sort(N, p))

