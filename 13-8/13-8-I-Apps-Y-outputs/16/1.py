
def get_hand_strength(hand):
    rank_count = {}
    for card in hand:
        rank = card[0]
        if rank not in rank_count:
            rank_count[rank] = 1
        else:
            rank_count[rank] += 1
    
    max_strength = 0
    for rank, count in rank_count.items():
        if count > max_strength:
            max_strength = count
    
    return max_strength

def main():
    hand = input("Enter five cards: ").split()
    print(get_hand_strength(hand))

if __name__ == '__main__':
    main()

