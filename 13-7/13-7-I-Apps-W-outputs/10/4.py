
def solve(N, X, D):
    # Calculate the sum of the sequence
    sum_of_seq = (N * (N + 1)) // 2
    # Calculate the sum of the elements taken by Takahashi
    takahashi_sum = X + (N - 1) * D
    # Calculate the sum of the elements taken by Aoki
    aoki_sum = sum_of_seq - takahashi_sum
    # Return the number of possible values of S - T
    return aoki_sum - takahashi_sum + 1

