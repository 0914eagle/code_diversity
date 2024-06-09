
def kth_smallest_divisor(n, k):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    
    if len(divisors) < k:
        return -1
    else:
        return divisors[k - 1]

# Read input
n, k = map(int, input().split())

# Call the function and print the result
result = kth_smallest_divisor(n, k)
print(result)
