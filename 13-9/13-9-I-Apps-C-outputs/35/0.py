
def longest_interesting_subsequence(N, S, A):
    # Initialize the longest interesting subsequence array
    li = [0] * N

    # Loop through the elements of the array
    for i in range(N):
        # If the current element is less than or equal to S,
        # the longest interesting subsequence starting with this element is 1
        if A[i] <= S:
            li[i] = 1
        # Otherwise, find the longest interesting subsequence starting with the previous element
        else:
            if i > 0:
                li[i] = li[i-1]
            else:
                li[i] = 0

    # Loop through the elements of the array in reverse order
    for i in range(N-1, -1, -1):
        # If the current element is less than or equal to S,
        # the longest interesting subsequence ending with this element is 1
        if A[i] <= S:
            li[i] = max(li[i], 1)
        # Otherwise, find the longest interesting subsequence ending with the next element
        else:
            if i < N-1:
                li[i] = max(li[i], li[i+1]+1)
            else:
                li[i] = max(li[i], 0)

    return li

