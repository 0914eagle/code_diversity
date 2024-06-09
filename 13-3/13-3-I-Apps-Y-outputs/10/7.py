
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
    print(0)
    exit()

# Initialize the current floor to the starting floor
current_floor = s

# Loop until we reach the goal floor
while current_floor != g:
    # If the current floor is less than the goal floor,
    # then we can press the UP button
    if current_floor < g:
        # Increment the current floor by the number of floors the UP button takes us
        current_floor += u
        # Increment the number of pushes
        pushes += 1
    # If the current floor is greater than the goal floor,
    # then we can press the DOWN button
    elif current_floor > g:
        # Decrement the current floor by the number of floors the DOWN button takes us
        current_floor -= d
        # Increment the number of pushes
        pushes += 1

# Print the number of pushes
print(pushes)

