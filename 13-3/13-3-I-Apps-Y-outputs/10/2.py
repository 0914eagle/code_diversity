
f, s, g, u, d = map(int, input().split())

# Initialize the variables
current_floor = s
pushes = 0

# Loop until we reach the goal floor or exceed the number of floors
while current_floor != g and current_floor <= f:
    # Check if we can reach the goal floor by pressing the UP button
    if current_floor + u <= g:
        current_floor += u
        pushes += 1
    # Check if we can reach the goal floor by pressing the DOWN button
    elif current_floor - d >= 1:
        current_floor -= d
        pushes += 1
    # If we cannot reach the goal floor, break the loop and print "use the stairs"
    else:
        break

# Print the number of pushes or "use the stairs"
if current_floor == g:
    print(pushes)
else:
    print("use the stairs")

