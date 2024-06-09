
def common_divisors(arr):
    # Find the greatest common divisor (GCD) of all elements in the array
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = gcd_recursive(gcd, arr[i])
    
    # Count the number of positive integers that divide each element in the array
    count = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            count += 1
    
    return count

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    print(common_divisors(arr))

