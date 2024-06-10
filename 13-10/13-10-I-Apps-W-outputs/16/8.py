
def get_smallest_sum(k):
    # find the smallest positive multiple of k
    multiple = 1
    while multiple * k <= 1000000:
        multiple += 1
    
    # get the decimal notation of the multiple
    decimal_notation = str(multiple * k)
    
    # sum the digits in the decimal notation
    sum_of_digits = 0
    for digit in decimal_notation:
        sum_of_digits += int(digit)
    
    return sum_of_digits

def main():
    k = int(input())
    print(get_smallest_sum(k))

if __name__ == '__main__':
    main()

