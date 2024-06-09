
def solve(N, strings):
    longest_sequence = 0
    for i in range(N):
        for j in range(i+1, N):
            if strings[j].startswith(strings[i]) and strings[j].endswith(strings[i]):
                longest_sequence = max(longest_sequence, j-i+1)
    return longest_sequence

