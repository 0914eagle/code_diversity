
def get_min_f(a, n):
    min_f = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                f = (i-j)**2 + g(a, i, j)**2
                if f < min_f:
                    min_f = f
    return min_f

def g(a, i, j):
    if i < j:
        return sum(a[i+1:j+1])
    else:
        return sum(a[j+1:i+1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_f(a, n))

