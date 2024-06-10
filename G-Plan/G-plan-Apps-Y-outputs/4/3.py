
def minimum_attacks_to_win(N, K, monsters_health):
    monsters_health.sort(reverse=True)
    total_attacks = sum(monsters_health) - sum(monsters_health[:K])
    return total_attacks

if __name__ == "__main__":
    N, K = map(int, input().split())
    monsters_health = list(map(int, input().split()))
    result = minimum_attacks_to_win(N, K, monsters_health)
    print(result)
