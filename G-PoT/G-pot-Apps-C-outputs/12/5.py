
def is_even(num):
    return num % 2 == 0

def find_winner(n, k, piles):
    total_cows = sum(piles)
    if total_cows % 2 == 1:
        return "Kevin"
    if k == 1:
        if n % 2 == 0:
            return "Nicky"
        else:
            return "Kevin"
    max_pile = max(piles)
    if max_pile <= total_cows // 2:
        return "Nicky"
    if is_even(max_pile):
        return "Kevin"
    return "Nicky"

n, k = map(int, input().split())
piles = list(map(int, input().split()))

winner = find_winner(n, k, piles)
print(winner)
