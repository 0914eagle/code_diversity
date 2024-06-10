ulate_rounds_won(n, alice_choices, bob_choices):
    min_rounds_won = max(alice_choices[1] - bob_choices[0], 0) + max(alice_choices[2] - bob_choices[1], 0) + max(alice_choices[0] - bob_choices[2], 0)
    max_rounds_won = min(alice_choices[1], bob_choices[2]) + min(alice_choices[2], bob_choices[0]) + min(alice_choices[0], bob_choices[1])
    return min_rounds_won, max_rounds_won

if __name__ == "__main__":
    n = int(input())
    alice_choices = list(map(int, input().split()))
    bob_choices = list(map(int, input().split()))
    
    min_won, max_won = calculate_rounds_won(n, alice_choices, bob_choices)
    print(min_won, max_won)
