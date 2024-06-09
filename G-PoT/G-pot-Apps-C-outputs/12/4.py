
def winner(n, k, piles):
    total_cows = sum(piles)
    
    if total_cows % 2 == 0:
        return "Nicky"
    
    if k == 1:
        if n % 2 == 0:
            return "Nicky"
        else:
            return "Kevin"
    else:
        max_pile = max(piles)
        if max_pile % 2 == 0:
            return "Kevin"
        else:
            return "Nicky"

# Read input
n, k = map(int, input().split())
piles = list(map(int, input().split()))

# Determine the winner
result = winner(n, k, piles)
print(result)
