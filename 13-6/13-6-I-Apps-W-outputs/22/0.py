
def find_divisible_number(array):
    # find the greatest common divisor of all elements in the array
    gcd = array[0]
    for i in range(1, len(array)):
        gcd = gcd_of_two_numbers(gcd, array[i])
    
    # check if the gcd is divisible by all elements in the array
    for i in range(len(array)):
        if array[i] % gcd != 0:
            return -1
    
    return gcd

def gcd_of_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return gcd_of_two_numbers(b, a % b)

def main():
    array = list(map(int, input().split()))
    print(find_divisible_number(array))

if __name__ == '__main__':
    main()

