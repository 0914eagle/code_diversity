
def get_cost(k, w):
    return k + (w-1) * 2 * k

def get_difference(n, w, k):
    return get_cost(k, w) - n

def get_borrowed_amount(n, w, k):
    difference = get_difference(n, w, k)
    if difference > 0:
        return difference
    else:
        return 0

if __name__ == '__main__':
    k, n, w = map(int, input().split())
    print(get_borrowed_amount(n, w, k))

