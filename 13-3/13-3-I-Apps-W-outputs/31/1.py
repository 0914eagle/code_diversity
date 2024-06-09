
def silver_coins(n, s):
    x, y = 0, 0
    coins = 0
    for move in s:
        if move == 'U':
            y += 1
        elif move == 'R':
            x += 1
        if x == y:
            coins += 1
    return coins

