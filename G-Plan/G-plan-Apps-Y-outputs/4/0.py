mum_attacks_to_win(N, K, health_values):
    health_values.sort(reverse=True)
    special_moves_used = 0
    total_attacks = 0
    
    for i in range(N):
        if i < K:
            special_moves_used += 1
        else:
            total_attacks += health_values[i]
    
    return total_attacks + special_moves_used

if __name__ == "__main__":
    N, K = map(int, input().split())
    health_values = list(map(int, input().split()))
    
    result = minimum_attacks_to_win(N, K, health_values)
    print(result)
