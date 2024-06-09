
def solve(N, A, B):
    # Initialize a list to store the sequence
    seq = []

    # Add the first element to the sequence
    seq.append(1)

    # Add elements to the sequence until it satisfies the conditions
    while len(seq) < N:
        # If the longest increasing subsequence of the current sequence is less than A, add an element that is greater than the last element of the sequence
        if len(longest_increasing_subsequence(seq)) < A:
            seq.append(seq[-1] + 1)
        # If the longest decreasing subsequence of the current sequence is less than B, add an element that is less than the last element of the sequence
        elif len(longest_decreasing_subsequence(seq)) < B:
            seq.append(seq[-1] - 1)
        # If both conditions are not satisfied, return -1
        else:
            return -1

    # If the sequence satisfies the conditions, return it
    return seq

# Find the longest increasing subsequence of a sequence
def longest_increasing_subsequence(seq):
    # Initialize a list to store the longest increasing subsequence
    lis = []

    # Add the first element to the list
    lis.append(seq[0])

    # Iterate over the remaining elements of the sequence
    for i in range(1, len(seq)):
        # If the current element is greater than the last element of the list, add it to the list
        if seq[i] > lis[-1]:
            lis.append(seq[i])
        # If the current element is less than or equal to the last element of the list, find the first element that is greater than the current element and insert it before that element
        else:
            for j in range(len(lis) - 1, -1, -1):
                if seq[i] > lis[j]:
                    lis.insert(j, seq[i])
                    break

    return lis

# Find the longest decreasing subsequence of a sequence
def longest_decreasing_subsequence(seq):
    # Initialize a list to store the longest decreasing subsequence
    lds = []

    # Add the first element to the list
    lds.append(seq[0])

    # Iterate over the remaining elements of the sequence
    for i in range(1, len(seq)):
        # If the current element is less than the last element of the list, add it to the list
        if seq[i] < lds[-1]:
            lds.append(seq[i])
        # If the current element is greater than or equal to the last element of the list, find the first element that is less than the current element and insert it before that element
        else:
            for j in range(len(lds) - 1, -1, -1):
                if seq[i] < lds[j]:
                    lds.insert(j, seq[i])
                    break

    return lds

