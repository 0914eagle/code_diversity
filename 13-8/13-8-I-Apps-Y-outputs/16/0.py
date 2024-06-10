
def get_hand_strength(hand):
    hand_ranks = [hand[i][0] for i in range(len(hand))]
    hand_suits = [hand[i][1] for i in range(len(hand))]
    hand_rank_count = {}
    for rank in hand_ranks:
        if rank in hand_rank_count:
            hand_rank_count[rank] += 1
        else:
            hand_rank_count[rank] = 1
    max_rank_count = max(hand_rank_count.values())
    return max_rank_count

def main():
    hand = input("Enter five cards: ").split()
    print(get_hand_strength(hand))

if __name__ == '__main__':
    main()

