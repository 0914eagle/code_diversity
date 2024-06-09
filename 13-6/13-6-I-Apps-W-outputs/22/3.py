
def get_divisible_number(arr):
    # Find the greatest common divisor of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = gcd(gcd, arr[i])
    
    # Check if the gcd is divisible by all elements in the array
    if all(arr[i] % gcd == 0 for i in range(len(arr))):
        return gcd
    else:
        return -1

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_divisible_number(arr))

if __name__ == '__main__':
    main()

