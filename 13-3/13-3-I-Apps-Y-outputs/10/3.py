
f, s, g, u, d = map(int, input().split())

# Initialize the minimum number of pushes to reach the goal
min_pushes = 0

# Initialize the current floor
current_floor = s

# Loop until the goal floor is reached or the maximum number of floors is reached
while current_floor != g and current_floor <= f:
    # Check if the UP button can be pressed
    if current_floor + u <= f:
        # Press the UP button and update the current floor
        current_floor += u
        min_pushes += 1
    # Check if the DOWN button can be pressed
    elif current_floor - d >= 1:
        # Press the DOWN button and update the current floor
        current_floor -= d
        min_pushes += 1
    # If neither button can be pressed, break the loop
    else:
        break

# If the goal floor is reached, print the minimum number of pushes
if current_floor == g:
    print(min_pushes)
# If the maximum number of floors is reached and the goal floor is not reached, print "use the stairs"
elif current_floor > f:
    print("use the stairs")

