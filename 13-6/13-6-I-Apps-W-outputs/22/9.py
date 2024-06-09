
def find_divisible_number(arr):
    # Find the greatest common divisor of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = gcd(gcd, arr[i])
    
    # Check if the gcd is divisible by all elements in the array
    for i in range(len(arr)):
        if arr[i] % gcd != 0:
            return -1
    
    return gcd

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_divisible_number(arr))

if __name__ == '__main__':
    main()

