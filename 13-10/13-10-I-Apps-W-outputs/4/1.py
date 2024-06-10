
def count_pairs(n, a, p):
    # Count the number of pairs of nodes (u, v) such that after swapping the apples of both nodes, Sagheer will win the game
    pairs = 0
    
    # Iterate over all pairs of nodes
    for i in range(1, n):
        for j in range(i+1, n+1):
            # Check if the swap will make Sagheer win the game
            if will_win(n, a, p, i, j):
                pairs += 1
    
    return pairs

def will_win(n, a, p, i, j):
    # Check if the swap will make Sagheer win the game
    # by simulating the game after the swap
    a_new = a.copy()
    a_new[i], a_new[j] = a_new[j], a_new[i]
    return simulate_game(n, a_new, p, i, j)

def simulate_game(n, a, p, i, j):
    # Simulate the game after the swap
    # i and j are the nodes that have been swapped
    if n == 2:
        # Base case: if there are only two nodes left, return True if Sagheer can win the game
        return a[i] > 0 and a[j] > 0
    else:
        # Recursive case: simulate the game for each child of i and j
        for k in range(1, n+1):
            if k != i and k != j:
                if simulate_game(n-1, a, p, k, k):
                    return True
        return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(count_pairs(n, a, p))

