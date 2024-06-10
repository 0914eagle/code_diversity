
def get_nearest_amount(candy_price, smallest_bill):
    # Calculate the nearest amount that Mirko can pay
    nearest_amount = candy_price - (candy_price % (10 ** smallest_bill))
    
    # If the nearest amount is not equal to the candy price, add the smallest bill to the nearest amount
    if nearest_amount != candy_price:
        nearest_amount += (10 ** smallest_bill)
    
    return nearest_amount

def main():
    candy_price, smallest_bill = map(int, input().split())
    print(get_nearest_amount(candy_price, smallest_bill))

if __name__ == '__main__':
    main()

