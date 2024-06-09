
n, m, k, x, y = map(int, input().split())

# Initialize variables to keep track of the maximum and minimum number of questions asked
max_questions = 0
min_questions = 1000000000000000000
sergei_asked = 0

# Iterate through each row
for i in range(1, n + 1):
    # If the current row is the same as the row where Sergei sits, then Sergei is asked
    if i == x:
        sergei_asked += 1
    
    # Iterate through each pupil in the current row
    for j in range(1, m + 1):
        # If the current pupil is the same as the pupil where Sergei sits, then Sergei is asked
        if j == y:
            sergei_asked += 1
        
        # Update the maximum and minimum number of questions asked
        max_questions = max(max_questions, i + j)
        min_questions = min(min_questions, i + j)

# Print the maximum, minimum, and number of times Sergei was asked
print(max_questions, min_questions, sergei_asked)

