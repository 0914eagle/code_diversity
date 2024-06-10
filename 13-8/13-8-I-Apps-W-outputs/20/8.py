
def get_kth_digit(k):
    # calculate the number of digits in the sequence up to the k-th digit
    num_digits = 1
    while num_digits < k:
        num_digits += 9 * 10 ** (num_digits - 1)
    
    # calculate the number that corresponds to the k-th digit
    num = 10 ** (num_digits - 1) + (k - 1) // num_digits
    
    # return the k-th digit of the number
    return str(num)[-1]

def main():
    k = int(input())
    print(get_kth_digit(k))

if __name__ == '__main__':
    main()

