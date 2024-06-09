
def solve(sequence, k):
    n = len(sequence)
    if n == 1:
        return 0
    if k == 0:
        return abs(sequence[0] - sequence[n-1])
    # find the maximum and minimum elements in the sequence
    max_element = max(sequence)
    min_element = min(sequence)
    # calculate the difference between the maximum and minimum elements
    diff = max_element - min_element
    # if we can perform the operation, try to increase or decrease the maximum element by one
    if k > 0:
        new_sequence = sequence[:]
        new_sequence[sequence.index(max_element)] += 1
        diff = min(diff, solve(new_sequence, k-1))
    # if we can perform the operation, try to increase or decrease the minimum element by one
    if k > 0:
        new_sequence = sequence[:]
        new_sequence[sequence.index(min_element)] -= 1
        diff = min(diff, solve(new_sequence, k-1))
    return diff

