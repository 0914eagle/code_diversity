
def get_divisible_number(arr):
    # Find the greatest common divisor of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = gcd_of_two_numbers(gcd, arr[i])
    
    # Check if the gcd is divisible by all elements in the array
    for i in range(len(arr)):
        if arr[i] % gcd != 0:
            return -1
    
    return gcd

def gcd_of_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return gcd_of_two_numbers(b, a % b)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_divisible_number(arr))

if __name__ == '__main__':
    main()

