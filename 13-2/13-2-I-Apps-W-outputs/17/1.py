
def solve(a, queries):
    # Initialize the number of inversions as zero
    inversions = 0

    # Loop through each query
    for l, r in queries:
        # Reverse the segment [l, r] of the permutation
        a[l:r+1] = a[l:r+1][::-1]

        # Count the number of inversions in the current permutation
        inversions = count_inversions(a)

        # Print whether the number of inversions is odd or even
        print("odd" if inversions % 2 == 1 else "even")

    return a

def count_inversions(a):
    # Initialize the number of inversions as zero
    inversions = 0

    # Loop through each element in the permutation
    for i in range(len(a)):
        # Loop through each element after the current element
        for j in range(i+1, len(a)):
            # If the current element is greater than the next element, increment the number of inversions
            if a[i] > a[j]:
                inversions += 1

    return inversions

