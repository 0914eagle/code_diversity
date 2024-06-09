
def get_input():
    n = int(input())
    cards = list(map(int, input().split()))
    return n, cards

def is_arithmetic_progression(cards):
    if len(cards) == 1:
        return True
    diff = cards[1] - cards[0]
    for i in range(2, len(cards)):
        if cards[i] - cards[i-1] != diff:
            return False
    return True

def get_missing_number(cards):
    if len(cards) == 1:
        return 1
    diff = cards[1] - cards[0]
    for i in range(2, len(cards)):
        if cards[i] - cards[i-1] != diff:
            return cards[i-1] + diff
    return cards[-1] + diff

def get_all_missing_numbers(cards):
    missing_numbers = []
    for i in range(len(cards)):
        missing_number = get_missing_number(cards[:i+1])
        if missing_number not in missing_numbers:
            missing_numbers.append(missing_number)
    return missing_numbers

def main():
    n, cards = get_input()
    if is_arithmetic_progression(cards):
        print(-1)
    else:
        missing_numbers = get_all_missing_numbers(cards)
        print(len(missing_numbers))
        print(*missing_numbers)

if __name__ == '__main__':
    main()

