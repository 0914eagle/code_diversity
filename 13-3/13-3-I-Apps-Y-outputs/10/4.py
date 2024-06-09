
f, s, g, u, d = map(int, input().split())

# Initialize the number of pushes to 0
pushes = 0

# If the start floor is greater than the goal floor, use the stairs
if s > g:
    print("use the stairs")
    exit()

# If the start floor is equal to the goal floor, no pushes are needed
if s == g:
    print(0)
    exit()

# If the start floor is less than the goal floor, calculate the number of pushes needed
while s != g:
    # If the start floor is less than the goal floor and the difference between the start floor and the goal floor is less than or equal to the up button, press the up button
    if s < g and g - s <= u:
        pushes += 1
        s += u
    # If the start floor is less than the goal floor and the difference between the start floor and the goal floor is greater than the up button, press the down button
    elif s < g and g - s > u:
        pushes += 1
        s -= d
    # If the start floor is greater than the goal floor and the difference between the start floor and the goal floor is less than or equal to the down button, press the down button
    elif s > g and s - g <= d:
        pushes += 1
        s -= d
    # If the start floor is greater than the goal floor and the difference between the start floor and the goal floor is greater than the down button, press the up button
    elif s > g and s - g > d:
        pushes += 1
        s += u

print(pushes)

