
def get_hand_strength(hand):
    hand_dict = {}
    for card in hand:
        rank = card[0]
        if rank not in hand_dict:
            hand_dict[rank] = 1
        else:
            hand_dict[rank] += 1

    max_strength = 0
    for rank, count in hand_dict.items():
        if count > max_strength:
            max_strength = count

    return max_strength

def main():
    hand = input("Enter five cards: ").split()
    print(get_hand_strength(hand))

if __name__ == '__main__':
    main()

