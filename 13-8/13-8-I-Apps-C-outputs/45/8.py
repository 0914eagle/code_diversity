
def get_purchases(cards_count, purchases):
    total_purchases = 0
    for child1, child2 in purchases:
        if cards_count[child1] + cards_count[child2] == 2:
            total_purchases += 1
            cards_count[child1] += 1
            cards_count[child2] += 1
    return total_purchases

def get_winners(cards_count, purchases):
    winners = []
    for child1, child2 in purchases:
        if cards_count[child1] + cards_count[child2] == 2:
            if cards_count[child1] > cards_count[child2]:
                winners.append((child1, 1))
            elif cards_count[child1] < cards_count[child2]:
                winners.append((child2, 1))
            else:
                winners.append((child1, 0))
                winners.append((child2, 0))
    return winners

def get_solution(cards_count, purchases):
    total_purchases = get_purchases(cards_count, purchases)
    winners = get_winners(cards_count, purchases)
    return total_purchases, winners

if __name__ == '__main__':
    num_children, num_purchases = map(int, input().split())
    cards_count = list(map(int, input().split()))
    purchases = []
    for _ in range(num_purchases):
        child1, child2 = map(int, input().split())
        purchases.append((child1, child2))
    total_purchases, winners = get_solution(cards_count, purchases)
    print(total_purchases)
    for winner in winners:
        print(*winner)

