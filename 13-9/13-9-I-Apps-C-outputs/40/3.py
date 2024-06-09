
def solve():
    N = int(input())
    a = list(map(int, input().split()))

    # Find the maximum amount of money that can be earned by smashing the gems
    max_money = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            max_money += a[i-1]

    return max_money

