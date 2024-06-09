
def chicken_for_dinner(N, M):
    if N == M:
        return f"Dr. Chaz will have {M} piece[s] of chicken left over!"
    elif N > M:
        return f"Dr. Chaz needs {N - M} more piece[s] of chicken!"
    else:
        return f"Dr. Chaz will have {M - N} piece[s] of chicken left over!"

