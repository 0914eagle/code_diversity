
def get_phone_numbers(cards):
    phone_numbers = []
    for i in range(len(cards) - 10):
        if cards[i] == "8" and cards[i + 1:i + 11].isdigit():
            phone_numbers.append(cards[i:i + 11])
    return phone_numbers

def get_max_phone_numbers(cards):
    phone_numbers = get_phone_numbers(cards)
    return len(phone_numbers)

def main():
    cards = input("Enter the cards with digits: ")
    print(get_max_phone_numbers(cards))

if __name__ == '__main__':
    main()

