mum_attacks_to_win(N, K, monster_healths):
    monster_healths.sort(reverse=True)
    special_moves_used = 0
    total_attacks = 0
    
    for health in monster_healths:
        if special_moves_used < K and health > 0:
            special_moves_used += 1
        else:
            total_attacks += health
    
    return total_attacks

if __name__ == "__main__":
    N, K = map(int, input().split())
    monster_healths = list(map(int, input().split()))
    
    result = minimum_attacks_to_win(N, K, monster_healths)
    print(result)
