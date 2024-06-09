
def f1(d, g, n, k):
    # Initialize variables
    max_coins = 0
    distracted_rounds = 0
    
    # Loop through each round
    for i in range(n):
        # If Gladstone is distracted, Donald can look at his cards and make a decision
        if i in range(k):
            distracted_rounds += 1
            # If Donald has more coins than Gladstone, he can win the round
            if d > g:
                max_coins += d
            # If Gladstone has more coins than Donald, Donald can't win the round
            else:
                max_coins += g
        # If Gladstone is not distracted, Donald can't see his cards and must bet all his coins
        else:
            max_coins += d
    
    # Return the maximum amount of coins Donald can be certain to have at the end of the game
    return max_coins

def f2(...):
    # Function to be called in the main function
    ...

if __name__ == '__main__':
    d, g, n, k = map(int, input().split())
    print(f1(d, g, n, k))

