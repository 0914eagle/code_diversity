
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

def get_possible_numbers(cards):
    if len(cards) == 1:
        return [-1]
    if is_arithmetic_progression(cards):
        return [1]
    diff = cards[1] - cards[0]
    possible_numbers = []
    for i in range(len(cards)):
        possible_numbers.append(cards[i] + (i+1) * diff)
    return possible_numbers

def main():
    n, cards = get_input()
    possible_numbers = get_possible_numbers(cards)
    if possible_numbers[0] == -1:
        print(-1)
    else:
        print(len(possible_numbers))
        print(*sorted(possible_numbers))

if __name__ == '__main__':
    main()

