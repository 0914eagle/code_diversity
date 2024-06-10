
def get_rounded_amount(candy_price, smallest_bill):
    # Calculate the nearest multiple of the smallest bill that is greater than or equal to the candy price
    rounded_amount = (candy_price // smallest_bill + 1) * smallest_bill
    return rounded_amount

def main():
    candy_price, smallest_bill = map(int, input().split())
    print(get_rounded_amount(candy_price, smallest_bill))

if __name__ == '__main__':
    main()

