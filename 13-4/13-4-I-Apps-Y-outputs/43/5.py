
def get_points(n, b, cards):
    points = 0
    for i in range(n):
        hand = cards[i*4:(i+1)*4]
        for card in hand:
            if card[1] == b:
                points += 11
            else:
                points += 10
    return points

