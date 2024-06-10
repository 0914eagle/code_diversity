
def get_dream_duration(n, s):
    # Initialize a list to store the dream duration for each step
    dream_duration = [0] * (n + 1)
    
    # Iterate through each step and check if Olga falls asleep
    for i in range(1, n + 1):
        # If Olga falls asleep, set the dream duration to -1
        if s[i - 1] == 'U' and i != 1:
            dream_duration[i] = -1
        # If Olga moves up or down, update the dream duration
        else:
            dream_duration[i] = dream_duration[i - 1] + 1
    
    return dream_duration

def get_input():
    n = int(input())
    s = input()
    return n, s

if __name__ == '__main__':
    n, s = get_input()
    dream_duration = get_dream_duration(n, s)
    for i in range(1, n + 1):
        print(dream_duration[i], end=" ")

