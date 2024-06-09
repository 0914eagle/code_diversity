
def get_cost(k, i):
    return i * k

def get_difference(n, w, k):
    total_cost = 0
    for i in range(1, w + 1):
        total_cost += get_cost(k, i)
    return total_cost - n

def main():
    k, n, w = map(int, input().split())
    print(get_difference(n, w, k))

if __name__ == '__main__':
    main()

