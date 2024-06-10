ulate_min_max_rounds(n, alice_choices, bob_choices):
    min_rounds = max(0, max(alice_choices[0] - bob_choices[2], 0) + max(alice_choices[1] - bob_choices[0], 0) + max(alice_choices[2] - bob_choices[1], 0))
    max_rounds = min(alice_choices[0], bob_choices[1]) + min(alice_choices[1], bob_choices[2]) + min(alice_choices[2], bob_choices[0])
    return min_rounds, max_rounds

if __name__ == '__main__':
    n = int(input())
    alice_choices = list(map(int, input().split()))
    bob_choices = list(map(int, input().split()))
    
    min_rounds, max_rounds = calculate_min_max_rounds(n, alice_choices, bob_choices)
    print(min_rounds, max_rounds