
import sys

N = int(input())
cards = list(map(int, input().split()))

# Alice's optimal strategy is to take the highest card
# Bob's optimal strategy is to take the lowest card

alice_score = sum(sorted(cards, reverse=True))
bob_score = sum(sorted(cards))

print(alice_score - bob_score)

