
def is_handsome(num):
    # Check if the number has only one digit
    if len(str(num)) == 1:
        return True
    
    # Check if the number has consecutive digits of different parity
    prev_digit = int(str(num)[0])
    for digit in str(num)[1:]:
        if prev_digit % 2 == digit % 2:
            return False
        prev_digit = int(digit)
    return True

def get_closest_handsome_number(num):
    # Find the closest handsome number that is smaller than the given number
    smaller_num = num
    while not is_handsome(smaller_num):
        smaller_num -= 1
    
    # Find the closest handsome number that is larger than the given number
    larger_num = num
    while not is_handsome(larger_num):
        larger_num += 1
    
    # Return the smaller and larger handsome numbers
    return smaller_num, larger_num

def main():
    num = int(input())
    smaller_num, larger_num = get_closest_handsome_number(num)
    print(smaller_num, larger_num)

if __name__ == '__main__':
    main()

