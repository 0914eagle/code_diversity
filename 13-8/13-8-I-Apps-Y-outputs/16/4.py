
def get_hand_strength(hand):
    hand = hand.split()
    rank_count = {}
    for card in hand:
        rank = card[0]
        if rank not in rank_count:
            rank_count[rank] = 1
        else:
            rank_count[rank] += 1
    
    max_rank = max(rank_count.values())
    return max_rank

def main():
    hand = input("Enter five cards: ")
    print(get_hand_strength(hand))

if __name__ == '__main__':
    main()

