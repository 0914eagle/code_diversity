
def get_cost(k, w):
    return k * w * (w + 1) // 2

def get_difference(k, n, w):
    return get_cost(k, w) - n

def main():
    k, n, w = map(int, input().split())
    print(get_difference(k, n, w))

if __name__ == '__main__':
    main()

