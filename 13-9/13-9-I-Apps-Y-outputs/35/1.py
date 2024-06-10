
def get_rounded_amount(candy_price, smallest_bill_zeros):
    # Convert the candy price to an integer
    candy_price = int(candy_price)
    
    # Get the smallest bill in units of Kunas
    smallest_bill = 10 ** smallest_bill_zeros
    
    # Round the candy price to the nearest bill
    rounded_amount = smallest_bill * (candy_price // smallest_bill)
    
    # If the candy price is not a multiple of the smallest bill, round up to the next bill
    if candy_price % smallest_bill != 0:
        rounded_amount += smallest_bill
    
    return rounded_amount

def main():
    candy_price, smallest_bill_zeros = input().split()
    rounded_amount = get_rounded_amount(candy_price, int(smallest_bill_zeros))
    print(rounded_amount)

if __name__ == '__main__':
    main()

