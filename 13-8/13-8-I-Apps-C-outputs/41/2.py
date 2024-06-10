
def is_shuffled(deck, n):
    # Function to check if the deck is shuffled
    # It will return True if the deck is shuffled, False otherwise
    for i in range(n):
        if deck[i] != i + 1:
            return False
    return True

def shuffle(deck, n):
    # Function to shuffle the deck
    # It will return the shuffled deck
    mid = n // 2
    left = deck[:mid]
    right = deck[mid:]
    shuffled_deck = []
    while left and right:
        shuffled_deck.append(left.pop())
        shuffled_deck.append(right.pop())
    shuffled_deck.extend(left)
    shuffled_deck.extend(right)
    return shuffled_deck

def shuffle_count(deck, n):
    # Function to find the minimum number of shuffles required to shuffle the deck
    count = 0
    while not is_shuffled(deck, n):
        deck = shuffle(deck, n)
        count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    deck = list(map(int, input().split()))
    print(shuffle_count(deck, n))

