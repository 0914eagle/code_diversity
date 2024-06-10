
def get_dream_duration(n, s):
    # Initialize a list to store the dream duration for each step
    dream_duration = [0] * (n + 1)
    
    # Set the initial direction of Olga's movement
    direction = 1 if s[0] == "U" else -1
    
    # Iterate through each step of the stairs
    for i in range(1, n + 1):
        # If Olga moves beyond the stairs, set the dream duration to -1
        if i == 1 and direction == -1 or i == n and direction == 1:
            dream_duration[i] = -1
            break
        
        # Update the dream duration for the current step
        dream_duration[i] = dream_duration[i - 1] + 1
        
        # Update the direction of Olga's movement based on the pointer above the current step
        if s[i - 1] == "U":
            direction = 1
        else:
            direction = -1
    
    return dream_duration

def main():
    n = int(input())
    s = input()
    dream_duration = get_dream_duration(n, s)
    print(*dream_duration, sep=" ")

if __name__ == '__main__':
    main()

