
def get_min_f(a, j):
    n = len(a)
    min_f = float('inf')
    for i in range(1, n + 1):
        if i != j:
            f = (i - j) ** 2 + g(a, i, j) ** 2
            if f < min_f:
                min_f = f
    return min_f

def g(a, i, j):
    if i < j:
        start = i
        end = j
    else:
        start = j
        end = i
    return sum(a[start:end + 1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    j = int(input())
    print(get_min_f(a, j))

