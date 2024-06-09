
n, m, k = map(int, input().split())
timetable = [list(map(int, input())) for _ in range(n)]

# Initialize the minimum number of hours spent in the university to infinity
min_hours = float('inf')

# Iterate over all possible combinations of skipped lessons
for skipped_lessons in range(k+1):
    # Initialize the number of hours spent in the university to 0
    hours = 0
    
    # Iterate over each day
    for day in range(n):
        # If there are no lessons on this day, continue to the next day
        if not any(timetable[day]):
            continue
        
        # If Ivan skips all lessons on this day, continue to the next day
        if skipped_lessons == m:
            continue
        
        # Calculate the number of hours spent in the university on this day
        hours += m - skipped_lessons
    
    # Update the minimum number of hours spent in the university if necessary
    min_hours = min(min_hours, hours)

print(min_hours)

