
def get_purchases(children, purchases):
    total_purchases = 0
    for purchase in purchases:
        child1, child2 = purchase
        if children[child1] == children[child2]:
            children[child1] += 1
            children[child2] += 1
            total_purchases += 1
        else:
            children[child1] += 2
            children[child2] += 2
            total_purchases += 2
    return total_purchases

def get_winners(children, purchases):
    winners = []
    for purchase in purchases:
        child1, child2 = purchase
        if children[child1] == children[child2]:
            winners.append((child1, child2, 0))
        else:
            winners.append((child1, child2, 1))
            winners.append((child2, child1, 2))
    return winners

def main():
    children, purchases = map(int, input().split())
    children = [0] * (children + 1)
    purchases = [tuple(map(int, input().split())) for _ in range(purchases)]
    total_purchases = get_purchases(children, purchases)
    winners = get_winners(children, purchases)
    print(total_purchases)
    for winner in winners:
        print(*winner)

if __name__ == '__main__':
    main()

