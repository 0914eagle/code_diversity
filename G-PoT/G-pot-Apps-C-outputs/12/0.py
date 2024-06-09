
n, k = map(int, input().split())
cows = list(map(int, input().split()))

# Count the number of odd piles
odd_piles = sum(1 for cow in cows if cow % 2 == 1)

# If there are an odd number of odd piles, Kevin wins
if odd_piles % 2 == 1:
    print("Kevin")
else:
    print("Nicky")
