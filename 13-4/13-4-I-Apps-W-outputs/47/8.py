
n, m, k = map(int, input().split())
timetable = [list(map(int, input())) for _ in range(n)]

# Initialize the minimum number of hours spent in the university to infinity
min_hours = float('inf')

# Iterate over all possible combinations of skipped lessons
for i in range(1 << n):
    # Convert the binary representation of the combination to a list of booleans
    skipped = [bool(i & (1 << j)) for j in range(n)]
    
    # Calculate the number of hours spent in the university for this combination
    hours = 0
    for day in range(n):
        if not skipped[day]:
            for hour in range(m):
                if timetable[day][hour] == 1:
                    hours += 1
    
    # Update the minimum number of hours spent in the university if necessary
    min_hours = min(min_hours, hours)

print(min_hours)

