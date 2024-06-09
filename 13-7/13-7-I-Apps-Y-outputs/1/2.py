
def get_min_score(N, K, M, A):
    # Calculate the sum of the scores already obtained
    total_score = sum(A)
    # Calculate the average score already obtained
    avg_score = total_score / (N-1)
    # Calculate the minimum score required on the final subject
    min_score = M - avg_score
    # If the minimum score is negative, it means the goal is unachievable
    if min_score < 0:
        return -1
    else:
        return min_score

