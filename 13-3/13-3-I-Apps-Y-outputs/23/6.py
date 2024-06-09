
import sys

n = int(input())
cards = list(map(int, input().split()))

# Alice's optimal strategy is to take the card with the highest value
alice_score = max(cards)

# Bob's optimal strategy is to take the card with the second highest value
bob_score = sorted(cards)[-2]

print(alice_score - bob_score)

