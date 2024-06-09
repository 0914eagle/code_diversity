
n, m, k, x, y = map(int, input().split())

# Initialize variables to keep track of the maximum and minimum number of questions asked
max_questions = 0
min_questions = 1000000000000000000

# Initialize a dictionary to keep track of the number of questions asked by each pupil
pupils = {}

# Iterate through the rows
for i in range(1, n + 1):
    # Iterate through the pupils in the current row
    for j in range(1, m + 1):
        # If the current pupil is Sergei, increment the number of times he is asked
        if i == x and j == y:
            pupils[(i, j)] = k
        # Otherwise, initialize the number of questions asked to 0
        else:
            pupils[(i, j)] = 0

# Iterate through the rows again
for i in range(1, n + 1):
    # Iterate through the pupils in the current row
    for j in range(1, m + 1):
        # If the current pupil is not Sergei, increment the number of questions asked
        if (i, j) not in pupils or pupils[(i, j)] < k:
            pupils[(i, j)] += 1
            # Update the maximum and minimum number of questions asked
            max_questions = max(max_questions, pupils[(i, j)])
            min_questions = min(min_questions, pupils[(i, j)])

# Print the maximum, minimum, and number of times Sergei was asked
print(max_questions, min_questions, k)

