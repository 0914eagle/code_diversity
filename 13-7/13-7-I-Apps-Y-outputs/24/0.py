
def get_coins(n, q, a, b):
    # Find the minimum number of coins needed to obtain the value b
    coins_needed = -1
    for i in range(n):
        if a[i] <= b:
            coins_needed = 1
            break
        else:
            coins_needed = -1
            break
    return coins_needed

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(q):
        print(get_coins(n, q, a, b[i]))

if __name__ == '__main__':
    main()

