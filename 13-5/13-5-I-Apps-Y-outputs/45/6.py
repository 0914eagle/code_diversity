
def round_to_nearest(price, smallest_bill):
    # Convert the price to a string
    price_str = str(price)
    
    # Find the index of the first non-zero digit in the price
    non_zero_index = 0
    for i in range(len(price_str)):
        if price_str[i] != '0':
            non_zero_index = i
            break
    
    # Find the number of zeros after the non-zero digit
    num_zeros = len(price_str) - non_zero_index - 1
    
    # Calculate the nearest amount that Mirko can pay
    nearest_amount = int(price_str[:non_zero_index] + '0' * (num_zeros - smallest_bill))
    
    return nearest_amount

def main():
    price, smallest_bill = map(int, input().split())
    print(round_to_nearest(price, smallest_bill))

if __name__ == '__main__':
    main()

