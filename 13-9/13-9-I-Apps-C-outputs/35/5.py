
def get_min_f_value(a, j):
    n = len(a)
    min_f_value = float('inf')
    for i in range(1, n+1):
        if i != j:
            f_value = (i-j)**2 + g(a, i, j)**2
            if f_value < min_f_value:
                min_f_value = f_value
    return min_f_value

def g(a, i, j):
    if i < j:
        i, j = j, i
    sum = 0
    for k in range(i+1, j+1):
        sum += a[k]
    return sum

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    j = int(input())
    print(get_min_f_value(a, j))

