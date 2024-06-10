
def calculate_minimum_loot_to_leave(k, coins):
    total_loot = sum(2**i * coins[i] for i in range(k))
    remaining_loot = total_loot
    for i in range(k - 1, -1, -1):
        loot_possible = min(remaining_loot // 2, 2**i * coins[i])
        remaining_loot -= loot_possible
    return remaining_loot % (10**9 + 7)

if __name__ == '__main__':
    k = int(input())
    coins = list(map(int, input().split()))
    print(calculate_minimum_loot_to_leave(k, coins))
