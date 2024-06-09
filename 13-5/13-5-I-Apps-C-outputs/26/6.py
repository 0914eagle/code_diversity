
def get_cards_sequence(oranges, apples):
    if oranges == 0 and apples == 0:
        return "Impossible"
    if oranges == 1 and apples == 1:
        return "AB"
    if oranges == 1 and apples > 1:
        return "A" + get_cards_sequence(0, apples-1)
    if oranges > 1 and apples == 1:
        return "B" + get_cards_sequence(oranges-1, 0)
    if oranges > 1 and apples > 1:
        return "AB" + get_cards_sequence(oranges-1, apples-1)

