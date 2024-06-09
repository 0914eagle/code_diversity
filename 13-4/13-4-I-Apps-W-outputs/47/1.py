
n, m, k = map(int, input().split())
timetable = [list(map(int, input())) for _ in range(n)]

# Initialize the minimum number of hours spent in the university to infinity
min_hours = float('inf')

# Loop through all possible combinations of skipped lessons
for skipped in range(k + 1):
    # Initialize the number of hours spent in the university to 0
    hours = 0
    
    # Loop through each day of the week
    for i in range(n):
        # If there are no lessons on this day, skip to the next day
        if not any(timetable[i]):
            continue
        
        # Find the first lesson that is not skipped
        first_lesson = next((j for j, lesson in enumerate(timetable[i], 1) if lesson and j not in range(1, skipped + 1)), None)
        
        # If there is no first lesson, skip to the next day
        if first_lesson is None:
            continue
        
        # Find the last lesson that is not skipped
        last_lesson = next((j for j, lesson in enumerate(timetable[i], first_lesson) if lesson and j not in range(first_lesson, skipped + 1)), None)
        
        # Add the number of hours spent in this day to the total
        hours += last_lesson - first_lesson + 1
    
    # Update the minimum number of hours spent in the university if necessary
    min_hours = min(min_hours, hours)

print(min_hours)

