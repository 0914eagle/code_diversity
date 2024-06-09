
def get_points(n, b, cards):
    points = 0
    for i in range(n):
        card1, card2 = cards[i*2], cards[i*2+1]
        if card1[1] == b:
            points += get_value(card1[0], True)
        else:
            points += get_value(card1[0], False)
        if card2[1] == b:
            points += get_value(card2[0], True)
        else:
            points += get_value(card2[0], False)
    return points

def get_value(card, is_dominant):
    if card == 'A':
        return 11 if is_dominant else 1
    elif card == 'K':
        return 4 if is_dominant else 4
    elif card == 'Q':
        return 3 if is_dominant else 3
    elif card == 'J':
        return 20 if is_dominant else 2
    elif card == 'T':
        return 10 if is_dominant else 10
    elif card == '9':
        return 14 if is_dominant else 0
    elif card == '8':
        return 0 if is_dominant else 0
    elif card == '7':
        return 0 if is_dominant else 0
    return 0

n, b = input().split()
n = int(n)
cards = []
for i in range(4*n):
    card = input()
    cards.append((card[0], card[1]))

print(get_points(n, b, cards))

