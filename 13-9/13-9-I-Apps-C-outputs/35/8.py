
def f(i, j, a):
    return (i - j) ** 2 + g(i, j, a) ** 2

def g(i, j, a):
    if i == j:
        return 0
    if i < j:
        return sum(a[i+1:j+1])
    else:
        return sum(a[j+1:i+1])

def get_min(a):
    n = len(a)
    min_val = float('inf')
    for i in range(1, n):
        for j in range(1, n):
            if i != j and f(i, j, a) < min_val:
                min_val = f(i, j, a)
    return min_val

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min(a))

