
def get_rounded_amount(candy_price, smallest_bill_power):
    # Find the nearest power of 10 that is greater than or equal to the candy price
    nearest_power = 10 ** smallest_bill_power
    while nearest_power < candy_price:
        nearest_power *= 10
    
    # Round the candy price to the nearest power of 10
    rounded_amount = nearest_power
    
    return rounded_amount

def main():
    candy_price, smallest_bill_power = map(int, input().split())
    rounded_amount = get_rounded_amount(candy_price, smallest_bill_power)
    print(rounded_amount)

if __name__ == '__main__':
    main()

