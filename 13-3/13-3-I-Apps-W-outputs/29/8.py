
import sys

def get_sum_modulo(n, k):
    # Calculate the sum of the first n numbers
    sum = (n * (n + 1)) // 2
    # Calculate the sum of the first k numbers
    sum_k = (k * (k + 1)) // 2
    # Calculate the sum of the first n-k numbers
    sum_n_k = (n - k) * (n - k + 1) // 2
    # Calculate the sum of the first n numbers minus the sum of the first k numbers
    sum_diff = sum - sum_k
    # Calculate the sum of the first n numbers minus the sum of the first n-k numbers
    sum_diff_n_k = sum - sum_n_k
    # Return the number of possible values of the sum, modulo (10^9+7)
    return (sum_diff * sum_diff_n_k) % 1000000007

n, k = map(int, input().split())
print(get_sum_modulo(n, k))

