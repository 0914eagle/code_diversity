
def round_candy(candy_cost, smallest_bill):
    # Find the nearest amount that Mirko can pay
    nearest_amount = int(candy_cost / 10 ** smallest_bill) * 10 ** smallest_bill
    
    # If the nearest amount is less than the candy cost, round up to the next power of 10
    if nearest_amount < candy_cost:
        nearest_amount *= 10
    
    return nearest_amount

def main():
    candy_cost, smallest_bill = map(int, input().split())
    print(round_candy(candy_cost, smallest_bill))

if __name__ == '__main__':
    main()

