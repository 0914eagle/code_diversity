
def get_cost(k, i):
    return i * k

def get_difference(k, n, w):
    total_cost = 0
    for i in range(1, w + 1):
        total_cost += get_cost(k, i)
    return total_cost - n

def main():
    k, n, w = map(int, input().split())
    print(get_difference(k, n, w))

if __name__ == '__main__':
    main()

