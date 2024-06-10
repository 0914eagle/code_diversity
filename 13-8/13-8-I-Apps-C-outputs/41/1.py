
def riffle_shuffle(deck):
    n = len(deck)
    mid = n // 2
    left, right = deck[:mid], deck[mid:]
    return left + right

def dovetail_shuffle(deck):
    n = len(deck)
    mid = n // 2
    left, right = deck[:mid], deck[mid:]
    return [left[i] for i in range(mid)] + [right[i] for i in range(mid)]

def shuffle_count(deck, shuffle_func):
    count = 0
    while True:
        deck = shuffle_func(deck)
        count += 1
        if deck == list(range(1, len(deck) + 1)):
            return count

def main():
    n = int(input())
    deck = list(map(int, input().split()))
    print(shuffle_count(deck, riffle_shuffle))
    print(shuffle_count(deck, dovetail_shuffle))

if __name__ == '__main__':
    main()

