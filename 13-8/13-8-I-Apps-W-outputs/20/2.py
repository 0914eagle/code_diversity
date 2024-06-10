
def get_kth_digit(k):
    # calculate the index of the digit in the number
    index = k - 1
    
    # calculate the number that contains the digit
    number = index // 10
    
    # calculate the remainder of the index divided by 10
    remainder = index % 10
    
    # return the digit
    return str(number)[remainder]

def main():
    k = int(input())
    print(get_kth_digit(k))

if __name__ == '__main__':
    main()

