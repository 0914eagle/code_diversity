
def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def f(i, j, a):
    return (i - j)**2 + g(i, j, a)**2

def g(i, j, a):
    if i < j:
        i, j = j, i
    sum = 0
    for k in range(i, j+1):
        sum += a[k]
    return sum

def solve(n, a):
    min_val = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                val = f(i, j, a)
                if val < min_val:
                    min_val = val
    return min_val

def main():
    n, a = read_input()
    print(solve(n, a))

if __name__ == '__main__':
    main()

