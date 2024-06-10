
def smallest_multiple_of_k(k):
    # find the smallest positive multiple of k
    multiple = k
    while multiple % k == 0:
        multiple += k
    
    # find the sum of the digits in the decimal notation of the multiple
    sum_of_digits = 0
    while multiple > 0:
        sum_of_digits += multiple % 10
        multiple //= 10
    
    return sum_of_digits

def main():
    k = int(input())
    print(smallest_multiple_of_k(k))

if __name__ == '__main__':
    main()

