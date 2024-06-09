
def get_phone_numbers(cards):
    phone_numbers = []
    for card in cards:
        if len(card) == 11 and card.startswith("8"):
            phone_numbers.append(card)
    return phone_numbers

def get_max_phone_numbers(cards):
    phone_numbers = get_phone_numbers(cards)
    return len(phone_numbers)

def main():
    n = int(input())
    cards = input()
    print(get_max_phone_numbers(cards))

if __name__ == '__main__':
    main()

