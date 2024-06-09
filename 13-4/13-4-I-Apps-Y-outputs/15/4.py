
def get_common_divisors(arr):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = gcd_helper(gcd, arr[i])
    
    # Return the number of positive integers that divide each element in the array
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    return count

def gcd_helper(a, b):
    if b == 0:
        return a
    else:
        return gcd_helper(b, a % b)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_common_divisors(arr))

