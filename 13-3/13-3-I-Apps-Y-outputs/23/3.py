
def solve():
    N = int(input())
    cards = list(map(int, input().split()))

    # Alice's optimal strategy is to take the card with the highest value
    # Bob's optimal strategy is to take the card with the lowest value
    # The difference in their scores will be the difference between the sum of Alice's cards and the sum of Bob's cards
    alice_score = sum(sorted(cards, reverse=True))
    bob_score = sum(sorted(cards))

    return alice_score - bob_score

