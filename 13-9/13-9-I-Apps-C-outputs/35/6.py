
def f(i, j, a):
    return (i - j)**2 + g(i, j, a)**2

def g(i, j, a):
    if i == j:
        return 0
    if i < j:
        return sum(a[i+1:j+1])
    else:
        return sum(a[j+1:i+1])

def solve(a):
    n = len(a)
    min_val = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                val = f(i, j, a)
                if val < min_val:
                    min_val = val
    return min_val

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

