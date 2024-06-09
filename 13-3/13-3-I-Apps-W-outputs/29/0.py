
import sys

def get_sum_count(n, k):
    # Calculate the number of possible values of the sum
    count = 1
    for i in range(k):
        count *= n - i
    # Calculate the number of possible values of the sum modulo (10^9+7)
    return count % (10**9 + 7)

n, k = map(int, input().split())
print(get_sum_count(n, k))

