
def convert_bitcoins_to_yen(bitcoins, exchange_rate):
    return bitcoins * exchange_rate

def get_total_gift_worth(gifts, exchange_rate):
    total_worth = 0
    for gift in gifts:
        if gift[1] == "JPY":
            total_worth += int(gift[0])
        elif gift[1] == "BTC":
            total_worth += convert_bitcoins_to_yen(float(gift[0]), exchange_rate)
    return total_worth

def main():
    exchange_rate = 380000.0
    gifts = []
    num_gifts = int(input())
    for i in range(num_gifts):
        gift = input().split()
        gifts.append(gift)
    total_worth = get_total_gift_worth(gifts, exchange_rate)
    print(total_worth)

if __name__ == '__main__':
    main()

