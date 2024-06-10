
def get_hand_strength(hand):
    hand_ranks = [card[0] for card in hand]
    hand_strength = len(set(hand_ranks))
    return hand_strength

def main():
    hand = input("Enter five-card hand: ").split()
    hand_strength = get_hand_strength(hand)
    print(f"Hand strength: {hand_strength}")

if __name__ == '__main__':
    main()

