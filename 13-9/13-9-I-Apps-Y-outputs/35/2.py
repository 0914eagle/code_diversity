
def round_to_nearest(candy_price, smallest_bill):
    # Convert the candy price to a string
    candy_price_str = str(candy_price)
    
    # Find the index of the first non-zero digit in the candy price
    first_non_zero_idx = 0
    for i in range(len(candy_price_str)):
        if candy_price_str[i] != '0':
            first_non_zero_idx = i
            break
    
    # Find the number of digits after the first non-zero digit
    num_digits = len(candy_price_str) - first_non_zero_idx
    
    # Find the nearest power of 10 that is greater than or equal to the number of digits
    nearest_power_of_10 = 1
    for i in range(smallest_bill):
        nearest_power_of_10 *= 10
    
    # Round the candy price to the nearest power of 10
    rounded_price = int(candy_price / nearest_power_of_10) * nearest_power_of_10
    
    return rounded_price

def main():
    candy_price, smallest_bill = map(int, input().split())
    print(round_to_nearest(candy_price, smallest_bill))

if __name__ == '__main__':
    main()

