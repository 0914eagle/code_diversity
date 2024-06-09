
def find_common_divisor(arr):
    # Find the greatest common divisor of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = find_gcd(gcd, arr[i])
    return gcd

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_common_divisor(arr))

if __name__ == '__main__':
    main()

