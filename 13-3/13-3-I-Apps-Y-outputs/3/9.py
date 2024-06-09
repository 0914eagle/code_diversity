
def f1(n, m, k, x_i, y_i, w_i, a_i, b_i):
    # your code here
    return total_cost

def f2(...):
    # your code here
    return ...

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    x_i, y_i, w_i = [], [], []
    a_i, b_i = [], []
    for _ in range(m):
        x_i.append(int(input()))
        y_i.append(int(input()))
        w_i.append(int(input()))
    for _ in range(k):
        a_i.append(int(input()))
        b_i.append(int(input()))
    total_cost = f1(n, m, k, x_i, y_i, w_i, a_i, b_i)
    print(total_cost)

