ulate_min_max_rounds(n, alice_counts, bob_counts):
    min_rounds = max(alice_counts[0] - bob_counts[2], 0) + max(alice_counts[1] - bob_counts[0], 0) + max(alice_counts[2] - bob_counts[1], 0)
    max_rounds = min(alice_counts[0], bob_counts[1]) + min(alice_counts[1], bob_counts[2]) + min(alice_counts[2], bob_counts[0])
    return min_rounds, max_rounds

if __name__ == "__main__":
    n = int(input())
    alice_counts = list(map(int, input().split()))
    bob_counts = list(map(int, input().split()))
    
    min_rounds, max_rounds = calculate_min_max_rounds(n, alice_counts, bob_counts)
    print(min_rounds, max_rounds