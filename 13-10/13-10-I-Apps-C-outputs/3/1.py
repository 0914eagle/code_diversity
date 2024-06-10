
def get_chaos(passengers, order):
    chaos = 0
    for i in order:
        chaos += passengers[i-1]
        chaos = chaos // 10 * 10
    return chaos

def get_max_chaos(passengers, orders):
    max_chaos = 0
    for order in orders:
        chaos = get_chaos(passengers, order)
        if chaos > max_chaos:
            max_chaos = chaos
    return max_chaos

def main():
    n = int(input())
    passengers = list(map(int, input().split()))
    orders = list(map(int, input().split()))
    print(get_max_chaos(passengers, orders))

if __name__ == '__main__':
    main()

