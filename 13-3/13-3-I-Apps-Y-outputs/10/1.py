
f, s, g, u, d = map(int, input().split())

# Initialize the variables
current_floor = s
button_pushes = 0

# Loop until we reach the goal floor or exceed the number of floors
while current_floor != g and current_floor <= f:
    # Check if we can reach the goal floor with the UP button
    if current_floor + u <= g:
        current_floor += u
        button_pushes += 1
    # Check if we can reach the goal floor with the DOWN button
    elif current_floor - d >= 1:
        current_floor -= d
        button_pushes += 1
    # If we cannot reach the goal floor with either button, we must use the stairs
    else:
        print("use the stairs")
        break

# Print the number of button pushes
else:
    print(button_pushes)

