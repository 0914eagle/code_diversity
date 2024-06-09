
n, m, k, x, y = map(int, input().split())

# Initialize variables to keep track of the maximum and minimum number of questions asked
max_questions = 0
min_questions = 1000000000000000000
sergei_asked = 0

# Iterate through each row
for i in range(1, n+1):
    # If the current row is the same as the row where Sergei sits, then the order of asking is reversed
    if i == x:
        order = range(m, 0, -1)
    else:
        order = range(1, m+1)
    
    # Iterate through each pupil in the current row
    for j in order:
        # If the current pupil is Sergei, then increment the number of times he was asked
        if i == x and j == y:
            sergei_asked += 1
        # If the current pupil has been asked more than the maximum number of times, then update the maximum number of times
        if k > max_questions:
            max_questions = k
        # If the current pupil has been asked less than the minimum number of times, then update the minimum number of times
        if k < min_questions:
            min_questions = k
        # Decrement the number of questions left to be asked
        k -= 1

# Print the maximum, minimum, and number of times Sergei was asked
print(max_questions, min_questions, sergei_asked)

