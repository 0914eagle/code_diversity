
def count_ways(N, A, cards):
    # Calculate the sum of the cards
    sum_cards = sum(cards)
    # Calculate the number of ways to select cards such that the average is A
    num_ways = 0
    for i in range(1, N+1):
        # Calculate the sum of the selected cards
        sum_selected = sum(cards[:i])
        # Calculate the sum of the unselected cards
        sum_unselected = sum_cards - sum_selected
        # Check if the average of the selected cards is A
        if sum_selected / i == A and sum_unselected / (N-i) == A:
            num_ways += 1
    return num_ways

def main():
    N, A = map(int, input().split())
    cards = list(map(int, input().split()))
    print(count_ways(N, A, cards))

if __name__ == '__main__':
    main()

