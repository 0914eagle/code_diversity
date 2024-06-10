
def get_dream_duration(n, s):
    # Initialize a list to store the dream duration for each step
    dream_duration = [0] * (n + 1)
    
    # Set the initial direction of the pointer
    direction = 1 if s[0] == "U" else -1
    
    # Iterate through each step
    for i in range(1, n + 1):
        # Calculate the dream duration for the current step
        dream_duration[i] = dream_duration[i - 1] + abs(direction)
        
        # Change the direction of the pointer
        direction = -direction
    
    # Return the dream duration for each step
    return dream_duration

def get_dream_duration_with_fall(n, s):
    # Get the dream duration for each step without the fall
    dream_duration = get_dream_duration(n, s)
    
    # Initialize a list to store the dream duration for each step with the fall
    dream_duration_with_fall = [0] * (n + 1)
    
    # Set the initial direction of the pointer
    direction = 1 if s[0] == "U" else -1
    
    # Iterate through each step
    for i in range(1, n + 1):
        # Calculate the dream duration for the current step with the fall
        dream_duration_with_fall[i] = dream_duration[i - 1] + abs(direction) + 1
        
        # Change the direction of the pointer
        direction = -direction
    
    # Return the dream duration for each step with the fall
    return dream_duration_with_fall

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(*get_dream_duration_with_fall(n, s), sep='\n')

