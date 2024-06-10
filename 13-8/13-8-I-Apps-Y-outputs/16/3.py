
def get_rank(card):
    rank_map = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13
    }
    return rank_map[card[0]]

def get_strength(hand):
    hand_ranks = [get_rank(card) for card in hand]
    hand_ranks_count = {}
    for rank in hand_ranks:
        if rank not in hand_ranks_count:
            hand_ranks_count[rank] = 1
        else:
            hand_ranks_count[rank] += 1
    max_strength = max(hand_ranks_count.values())
    return max_strength

def main():
    hand = input().split()
    strength = get_strength(hand)
    print(strength)

if __name__ == '__main__':
    main()

