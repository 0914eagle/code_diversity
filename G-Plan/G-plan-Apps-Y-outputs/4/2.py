mum_attacks_to_win(N, K, health_values):
    health_values.sort(reverse=True)
    special_moves = min(K, N - 1)
    total_attacks = sum(health_values[special_moves:])
    return total_attacks

if __name__ == "__main__":
    N, K = map(int, input().split())
    health_values = list(map(int, input().split()))
    result = minimum_attacks_to_win(N, K, health_values)
    print(result)
