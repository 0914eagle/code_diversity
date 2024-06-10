
import itertools

def get_playable_cards(cards, slots):
    playable_cards = []
    for card in cards:
        if card in slots:
            playable_cards.append(card)
    return playable_cards

def get_next_turn(cards, slots, discarded_cards):
    playable_cards = get_playable_cards(cards, slots)
    if len(playable_cards) == 0:
        return None
    else:
        return playable_cards[0]

def get_slot_value(slot):
    if slot == "A":
        return 1
    elif slot == "J":
        return 11
    elif slot == "Q":
        return 12
    elif slot == "K":
        return 13
    else:
        return int(slot)

def get_lowest_slot(slots):
    lowest_slot = None
    lowest_value = 14
    for slot in slots:
        value = get_slot_value(slot)
        if value < lowest_value:
            lowest_slot = slot
            lowest_value = value
    return lowest_slot

def get_slot_status(slots, discarded_cards):
    status = []
    for slot in slots:
        if slot in discarded_cards:
            status.append("X")
        else:
            status.append("_")
    return "".join(status)

def get_result(cards, slots, discarded_cards):
    status = get_slot_status(slots, discarded_cards)
    if "X" not in status:
        return "Theta wins"
    else:
        return "Theta loses"

def main():
    deck = input()
    cards = list(deck)
    slots = list(itertools.combinations(cards, 10))
    discarded_cards = []
    while len(slots) > 0:
        card = get_next_turn(cards, slots, discarded_cards)
        if card is None:
            break
        slot = get_lowest_slot(slots)
        slots.remove(slot)
        discarded_cards.append(slot)
    print(get_result(cards, slots, discarded_cards))

if __name__ == '__main__':
    main()

