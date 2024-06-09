
def is_even(num):
    return num % 2 == 0

def can_win(n, k, piles):
    total_cows = sum(piles)
    if total_cows % 2 == 1:
        return "Kevin"
    if k == 1:
        if n % 2 == 0:
            return "Nicky"
        else:
            return "Kevin"
    if n % 2 == 0:
        return "Nicky"
    return "Kevin"

n, k = map(int, input().split())
piles = list(map(int, input().split()))

print(can_win(n, k, piles))
