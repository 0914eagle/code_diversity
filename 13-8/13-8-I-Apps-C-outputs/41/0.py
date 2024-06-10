
def get_shuffle_count(deck):
    shuffle_count = 0
    while not is_ordered(deck):
        shuffle_count += 1
        deck = shuffle(deck)
    return shuffle_count

def shuffle(deck):
    mid = len(deck) // 2
    return deck[:mid] + deck[mid:]

def is_ordered(deck):
    for i in range(len(deck) - 1):
        if deck[i] > deck[i + 1]:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    deck = list(map(int, input().split()))
    print(get_shuffle_count(deck))

