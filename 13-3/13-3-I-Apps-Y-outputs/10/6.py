
f, s, g, u, d = map(int, input().split())

# Initialize the number of pushes to 0
pushes = 0

# If the starting floor is greater than the goal floor,
# then we can't reach the goal floor with the elevator
if s > g:
    print("use the stairs")
    exit()

# If the starting floor is equal to the goal floor,
# then we don't need to push any buttons
if s == g:
    print(pushes)
    exit()

# Initialize the current floor to the starting floor
current_floor = s

# While the current floor is not equal to the goal floor,
# keep pushing buttons
while current_floor != g:
    # If the current floor is less than the goal floor,
    # push the UP button
    if current_floor < g:
        current_floor += u
        pushes += 1
    # If the current floor is greater than the goal floor,
    # push the DOWN button
    else:
        current_floor -= d
        pushes += 1

# If the current floor is equal to the goal floor,
# then we have reached the goal floor
if current_floor == g:
    print(pushes)
# If the current floor is not equal to the goal floor,
# then we cannot reach the goal floor with the elevator
else:
    print("use the stairs")

