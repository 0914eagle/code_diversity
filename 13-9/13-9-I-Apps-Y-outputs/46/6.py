
def solution(n, a):
    # Step 1: Find the leftmost and rightmost indices of books on the shelf
    leftmost = 0
    rightmost = 0
    for i in range(n):
        if a[i] == 1:
            leftmost = i
            break
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            rightmost = i
            break
    
    # Step 2: Initialize the minimum number of moves to collect all the books as 0
    min_moves = 0
    
    # Step 3: Loop until all the books are collected as a contiguous segment
    while leftmost <= rightmost:
        # Step 3.1: Shift the segment [leftmost, rightmost] to the right by 1
        a[rightmost+1] = 1
        a[leftmost:rightmost+1] = [0] * (rightmost-leftmost+1)
        leftmost += 1
        rightmost += 1
        min_moves += 1
    
    # Step 4: Return the minimum number of moves required to collect all the books as a contiguous segment
    return min_moves

