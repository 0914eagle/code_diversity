
def get_strength(hand):
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    rank_counts = {}
    for rank in ranks:
        if rank not in rank_counts:
            rank_counts[rank] = 1
        else:
            rank_counts[rank] += 1
    max_strength = 0
    for rank, count in rank_counts.items():
        if count > max_strength:
            max_strength = count
    return max_strength

def main():
    hand = input("Enter five-card hand: ").split()
    print(get_strength(hand))

if __name__ == '__main__':
    main()

