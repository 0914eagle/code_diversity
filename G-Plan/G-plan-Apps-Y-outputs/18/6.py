ulate_min_max_wins(n, alice_choices, bob_choices):
    min_wins = max(0, alice_choices[0] - bob_choices[2]) + max(0, alice_choices[1] - bob_choices[0]) + max(0, alice_choices[2] - bob_choices[1])
    max_wins = min(alice_choices[0], bob_choices[1]) + min(alice_choices[1], bob_choices[2]) + min(alice_choices[2], bob_choices[0])
    return min_wins, max_wins

if __name__ == "__main__":
    n = int(input())
    alice_choices = list(map(int, input().split()))
    bob_choices = list(map(int, input().split()))
    
    min_wins, max_wins = calculate_min_max_wins(n, alice_choices, bob_choices)
    print(min_wins, max_wins)
