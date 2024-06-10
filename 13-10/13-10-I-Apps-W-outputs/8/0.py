
def get_largest_number_divisible_by_90(cards):
    largest_number = 0
    for i in range(len(cards)):
        for j in range(i, len(cards)):
            number = int("".join(map(str, cards[i:j+1])))
            if number % 90 == 0 and number > largest_number:
                largest_number = number
    return largest_number

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    print(get_largest_number_divisible_by_90(cards))

if __name__ == '__main__':
    main()

