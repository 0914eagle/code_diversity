
def solve(n, x, d):
    # Calculate the sum of the sequence
    sum_seq = (n * (n + 1)) // 2
    # Calculate the sum of the elements taken by Takahashi
    sum_takahashi = x + (n - 1) * d
    # Calculate the sum of the elements taken by Aoki
    sum_aoki = sum_seq - sum_takahashi
    # Return the number of possible values of S - T
    return sum_aoki

