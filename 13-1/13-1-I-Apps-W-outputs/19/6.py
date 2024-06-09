
n, m, k, x, y = map(int, input().split())

# Initialize variables to keep track of the maximum and minimum number of questions asked
max_questions = 0
min_questions = 1000000000000000000
sergei_asked = 0

# Iterate through each row
for i in range(1, n + 1):
    # If the current row is the same as the row where Sergei sits, then the order of asking is reversed
    if i == x:
        order = range(m, 0, -1)
    else:
        order = range(1, m + 1)
    
    # Iterate through each pupil in the current row
    for j in order:
        # If the current pupil is Sergei, then increment the number of times he was asked
        if i == x and j == y:
            sergei_asked += 1
        # If the current pupil was asked, then increment the maximum and minimum number of questions asked
        if k > 0:
            max_questions = max(max_questions, k)
            min_questions = min(min_questions, k)
            k -= 1

# Print the results
print(max_questions, min_questions, sergei_asked)

