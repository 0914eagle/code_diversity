
def solve(n, T, times):
    # Calculate the probability of solving each crossword
    probabilities = [1 / 2] * len(times)

    # Calculate the expected number of crosswords solved
    expected = 0
    for i in range(len(times)):
        expected += i * probabilities[i]

    # Calculate the expected number of crosswords solved in T seconds
    expected_in_T_seconds = expected * T

    # Calculate the answer
    answer = expected_in_T_seconds * 1000000007

    return answer

