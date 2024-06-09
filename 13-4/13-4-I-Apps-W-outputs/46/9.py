
def get_cost(k, w):
    return k + (w - 1) * 2 * k

def get_difference(n, cost):
    return cost - n

def get_borrowed_amount(n, k, w):
    cost = get_cost(k, w)
    difference = get_difference(n, cost)
    if difference > 0:
        return difference
    else:
        return 0

if __name__ == '__main__':
    k, n, w = map(int, input().split())
    print(get_borrowed_amount(n, k, w))

