
def f1(n, a):
    # f1 function to find the initial order of the cubes
    order = [0] * n
    for i in range(n):
        order[a[i]-1] = i+1
    return order

def f2(n, a):
    # f2 function to find the current order of the cubes
    order = [0] * n
    for i in range(n):
        order[i] = a[n-i-1]
    return order

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    order = f1(n, a)
    print(*order)

