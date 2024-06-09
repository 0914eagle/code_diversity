
def kth_smallest_divisor(n, k):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    
    if len(divisors) < k:
        return -1
    else:
        return divisors[k-1]

n, k = map(int, input().split())
result = kth_smallest_divisor(n, k)
print(result)
