
def solve(N, X, D):
    # Calculate the sum of the sequence
    sum_of_sequence = (N * (N + 1)) // 2
    # Calculate the sum of the elements taken by Takahashi
    sum_of_takahashi = X + (N - 1) * D
    # Calculate the sum of the elements taken by Aoki
    sum_of_aoki = sum_of_sequence - sum_of_takahashi
    # Return the number of possible values of S - T
    return sum_of_aoki

