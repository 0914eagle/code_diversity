
def solve(a, k):
    n = len(a)
    # Step 1: Sort the array in non-decreasing order
    a.sort()
    # Step 2: Initialize the number of moves to 0
    moves = 0
    # Step 3: Loop through the array and find the minimum number of moves required to obtain at least k equal elements
    for i in range(n):
        # If the current element is equal to the k-th element, break the loop
        if a[i] == a[k-1]:
            break
        # If the current element is greater than the k-th element, we need to decrease the current element by 1
        elif a[i] > a[k-1]:
            moves += 1
            a[i] -= 1
        # If the current element is less than the k-th element, we need to increase the current element by 1
        else:
            moves += 1
            a[i] += 1
    return moves

