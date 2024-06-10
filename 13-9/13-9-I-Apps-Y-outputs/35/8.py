
def get_rounded_amount(candy_price, smallest_bill):
    # Calculate the nearest amount that Mirko can pay
    nearest_amount = (candy_price // smallest_bill) * smallest_bill
    
    # If the nearest amount is less than the candy price, add the smallest bill to it
    if nearest_amount < candy_price:
        nearest_amount += smallest_bill
    
    return nearest_amount

def main():
    candy_price, smallest_bill = map(int, input().split())
    print(get_rounded_amount(candy_price, smallest_bill))

if __name__ == '__main__':
    main()

