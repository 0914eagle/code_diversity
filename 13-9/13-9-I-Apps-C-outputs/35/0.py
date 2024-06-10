
def f(i, j, a):
    return (i - j)**2 + g(i, j, a)**2

def g(i, j, a):
    if i == j:
        return 0
    if i < j:
        return sum(a[i+1:j+1])
    else:
        return sum(a[j+1:i+1])

def solve(n, a):
    min_value = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                value = f(i, j, a)
                if value < min_value:
                    min_value = value
    return min_value

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

