mum_attacks_to_win(N, K, monsters_health):
    monsters_health.sort(reverse=True)
    total_attacks = 0
    
    for i in range(K, N):
        total_attacks += monsters_health[i]
    
    return total_attacks

if __name__ == "__main__":
    N, K = map(int, input().split())
    monsters_health = list(map(int, input().split()))
    
    result = minimum_attacks_to_win(N, K, monsters_health)
    print(result)
