
def read_array(n):
    return list(map(int, input().split()))

def f(i, j, a):
    return (i - j) ** 2 + g(i, j, a) ** 2

def g(i, j, a):
    if i == j:
        return 0
    if i < j:
        return sum(a[i+1:j+1])
    else:
        return sum(a[j+1:i+1])

def get_min_f(n, a):
    min_f = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                f_val = f(i, j, a)
                if f_val < min_f:
                    min_f = f_val
    return min_f

def main():
    n = int(input())
    a = read_array(n)
    print(get_min_f(n, a))

if __name__ == '__main__':
    main()

