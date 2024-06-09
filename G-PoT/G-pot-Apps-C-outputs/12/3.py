
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Function to check if a player can win from a given game state
def can_win(a):
    xor_sum = 0
    for num in a:
        xor_sum ^= num
    if xor_sum == 0:
        return False
    if xor_sum > 0 and len(a) % 2 == 0:
        return True
    if xor_sum > 0 and len(a) % 2 != 0:
        return False

# Check if Kevin can win from the initial game state
if can_win(a):
    print("Kevin")
else:
    print("Nicky")
