
def get_min_value(a):
    n = len(a)
    min_value = float('inf')
    for i in range(n):
        for j in range(n):
            if i != j:
                value = (i - j) ** 2 + g(a, i, j) ** 2
                if value < min_value:
                    min_value = value
    return min_value

def g(a, i, j):
    return sum(a[k] for k in range(min(i, j) + 1, max(i, j) + 1))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_value(a))

