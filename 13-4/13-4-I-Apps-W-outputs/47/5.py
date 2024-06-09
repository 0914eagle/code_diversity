
n, m, k = map(int, input().split())
timetable = [list(map(int, input())) for _ in range(n)]

# Initialize the number of hours spent in the university to 0
hours = 0

# Loop through each day of the week
for i in range(n):
    # Initialize the number of lessons skipped to 0
    skipped = 0
    
    # Loop through each hour of the day
    for j in range(m):
        # If there is a lesson and Ivan hasn't skipped enough lessons, skip the lesson
        if timetable[i][j] == 1 and skipped < k:
            skipped += 1
        # Otherwise, increment the number of hours spent in the university
        else:
            hours += 1

# Print the minimum number of hours Ivan has to spend in the university during the week
print(hours)

