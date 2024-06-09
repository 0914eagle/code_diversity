
def get_expected_inversions(n, p):
    # Initialize the number of inversions as 0
    inversions = 0

    # Loop through each element in the array
    for i in range(n):
        # If the current element is not -1, skip it
        if p[i] != -1:
            continue
        # If the current element is -1, find the number of inversions it creates
        inversions += count_inversions(p, i)

    # Return the expected number of inversions
    return inversions

def count_inversions(p, i):
    # Initialize the number of inversions as 0
    inversions = 0

    # Loop through each element after the current element
    for j in range(i+1, len(p)):
        # If the current element is not -1 and is less than the previous element, increment the number of inversions
        if p[j] != -1 and p[j] < p[i]:
            inversions += 1

    # Return the number of inversions
    return inversions

n = int(input())
p = list(map(int, input().split()))

# Call the get_expected_inversions function and print the result
print(get_expected_inversions(n, p))

