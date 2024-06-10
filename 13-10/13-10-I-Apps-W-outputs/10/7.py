
def get_dream_duration(n, s):
    # Initialize the dream duration for each step
    dream_duration = [0] * (n + 1)
    
    # Set the initial step and direction
    step = 1
    direction = 1 if s[0] == "U" else -1
    
    # Iterate through each step
    for i in range(1, n):
        # If Olga moves beyond the stairs, break the loop
        if step == 1 and direction == -1 or step == n and direction == 1:
            break
        
        # Update the dream duration for the current step
        dream_duration[step] = i
        
        # Update the direction and step
        direction = -direction
        step += direction
    
    # Return the dream duration for each step
    return dream_duration

def get_dream_duration_wrapper():
    n = int(input())
    s = input()
    return get_dream_duration(n, s)

if __name__ == '__main__':
    dream_duration = get_dream_duration_wrapper()
    for i in range(len(dream_duration)):
        print(dream_duration[i], end=" ")

