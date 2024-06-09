
def solve(seq, jump, k, q, left, right):
    # Initialize the array with zeros
    seq = [0] * len(seq)

    # Call the procedure exactly k times
    for i in range(k):
        i = 0
        while i < len(seq):
            seq[i] += 1
            i += jump

    # Find the sum of elements between left and right for each special part
    result = []
    for l, r in zip(left, right):
        result.append(sum(seq[l:r+1]))

    return result

