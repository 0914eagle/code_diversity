
def get_hand_strength(hand):
    hand = hand.split()
    hand_ranks = list(map(lambda x: x[0], hand))
    hand_suits = list(map(lambda x: x[1], hand))
    hand_ranks = list(set(hand_ranks))
    max_rank = max(hand_ranks)
    count = hand_ranks.count(max_rank)
    return count

def main():
    hand = input("Enter hand: ")
    print(get_hand_strength(hand))

if __name__ == '__main__':
    main()

