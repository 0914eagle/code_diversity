
def round_to_nearest_bill(candy_price, smallest_bill_zeros):
    # Convert the candy price to an integer
    candy_price = int(candy_price)
    
    # Find the nearest bill that Mirko has
    nearest_bill = 10 ** smallest_bill_zeros
    
    # Round the candy price to the nearest bill
    rounded_price = nearest_bill * (candy_price // nearest_bill)
    
    # If the candy price is not a multiple of the nearest bill, round up to the next bill
    if candy_price % nearest_bill != 0:
        rounded_price += nearest_bill
    
    return rounded_price

def main():
    candy_price, smallest_bill_zeros = map(int, input().split())
    print(round_to_nearest_bill(candy_price, smallest_bill_zeros))

if __name__ == '__main__':
    main()

