
def minimum_attacks_to_win(N, K, monsters):
    monsters.sort(reverse=True)
    special_moves = min(K, N - 1)
    total_attacks = sum(monster - 1 for monster in monsters[special_moves:])
    return total_attacks

if __name__ == "__main__":
    N, K = map(int, input().split())
    monsters = list(map(int, input().split()))
    result = minimum_attacks_to_win(N, K, monsters)
    print(result)
