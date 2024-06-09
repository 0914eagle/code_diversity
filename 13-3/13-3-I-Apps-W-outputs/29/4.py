
import sys

def get_sum_count(n, k):
    # Calculate the sum of the first n numbers
    sum = (n * (n + 1)) // 2
    # Calculate the sum of the last k numbers
    last_sum = (k * (k + 1)) // 2
    # Calculate the sum of the first n - k numbers
    first_sum = (n - k) * (n - k + 1) // 2
    # Calculate the sum of the middle k numbers
    middle_sum = last_sum - first_sum
    # Calculate the total number of possible values
    count = (sum - middle_sum) % (10**9 + 7)
    return count

n, k = map(int, input().split())
print(get_sum_count(n, k))

