mum_attacks_to_win(N, K, monster_healths):
    monster_healths.sort(reverse=True)
    special_moves = min(K, N - 1)
    total_attacks = sum(monster_healths[special_moves:])
    return total_attacks

if __name__ == "__main__":
    N, K = map(int, input().split())
    monster_healths = list(map(int, input().split()))
    result = minimum_attacks_to_win(N, K, monster_healths)
    print(result)
