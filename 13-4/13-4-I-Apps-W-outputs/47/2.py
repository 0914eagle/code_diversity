
n, m, k = map(int, input().split())
timetable = [list(map(int, input())) for _ in range(n)]

# Initialize the minimum number of hours spent in the university to infinity
min_hours = float('inf')

# Loop through all possible combinations of skipped lessons
for i in range(1 << n):
    # Convert the binary representation of the combination to a list of booleans
    skipped = [bool(i & (1 << j)) for j in range(n)]
    
    # Initialize the number of hours spent in the university to 0
    hours = 0
    
    # Loop through each day
    for day in range(n):
        # If the lesson is not skipped, add the number of hours spent in the university for that day
        if not skipped[day]:
            hours += timetable[day].count(1)
    
    # If the number of hours spent in the university is less than the minimum, update the minimum
    if hours < min_hours:
        min_hours = hours

print(min_hours)

