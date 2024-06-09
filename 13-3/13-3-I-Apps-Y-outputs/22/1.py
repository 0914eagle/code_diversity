
def f1(N, A, x):
    # Calculate the sum of the integers written on the cards
    sum_x = sum(x)

    # Calculate the average of the integers written on the cards
    avg_x = sum_x / N

    # Check if the average is equal to A
    if avg_x == A:
        return 1
    else:
        return 0

def f2(N, A, x):
    # Initialize a variable to store the number of ways to select cards
    num_ways = 0

    # Iterate over all possible combinations of cards
    for i in range(1, 2**N):
        # Convert the binary representation of i to a list of indices of selected cards
        selected_cards = [j for j in range(N) if i & (1 << j)]

        # Calculate the sum of the integers written on the selected cards
        sum_selected = sum([x[j] for j in selected_cards])

        # Calculate the average of the integers written on the selected cards
        avg_selected = sum_selected / len(selected_cards)

        # Check if the average is equal to A
        if avg_selected == A:
            num_ways += 1

    return num_ways

if __name__ == '__main__':
    N, A = map(int, input().split())
    x = list(map(int, input().split()))
    print(f2(N, A, x))

