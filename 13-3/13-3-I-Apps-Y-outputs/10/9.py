
f, s, g, u, d = map(int, input().split())

# Initialize the minimum number of pushes to reach the goal
min_pushes = 0

# Initialize the current floor
current_floor = s

# Loop until the goal floor is reached or the maximum number of floors is reached
while current_floor != g and current_floor <= f:
    # If the current floor is less than the goal floor, press the UP button
    if current_floor < g:
        current_floor += u
        min_pushes += 1
    # If the current floor is greater than the goal floor, press the DOWN button
    else:
        current_floor -= d
        min_pushes += 1

# If the goal floor is not reached, print "use the stairs"
if current_floor != g:
    print("use the stairs")
# Otherwise, print the minimum number of pushes
else:
    print(min_pushes)

