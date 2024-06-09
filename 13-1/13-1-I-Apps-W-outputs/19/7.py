
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
        # If the current pupil is the same as Sergei, then increment the number of times Sergei was asked
        if i == x and j == y:
            sergei_asked += 1
        
        # Update the maximum and minimum number of questions asked
        max_questions = max(max_questions, k)
        min_questions = min(min_questions, k)
        
        # Decrement the number of questions left to ask
        k -= 1
        
        # If there are no more questions left to ask, break the loop
        if k == 0:
            break
    
    # If there are no more questions left to ask, break the loop
    if k == 0:
        break

# Print the results
print(max_questions, min_questions, sergei_asked)

