
def solve(N, X, D):
    # Calculate the sum of the sequence
    sum_of_seq = (N * (N + 1)) // 2
    # Calculate the sum of the elements taken by Takahashi
    sum_takahashi = X + (N - 1) * D
    # Calculate the sum of the elements taken by Aoki
    sum_aoki = sum_of_seq - sum_takahashi
    # Return the number of possible values of S - T
    return sum_aoki - sum_takahashi + 1

