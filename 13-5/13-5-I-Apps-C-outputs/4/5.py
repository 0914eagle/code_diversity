
def get_earliest_time(lights):
    # Initialize variables
    n = len(lights)
    time = 0
    on_lights = 0
    off_lights = 0
    
    # Loop through each light
    for i in range(n):
        # Check if the light is on or off
        if lights[i] == "1":
            on_lights += 1
        else:
            off_lights += 1
        
        # Check if all lights are on
        if on_lights == n:
            break
        
        # Increment time
        time += 1
    
    # Return the earliest time
    return time

def main():
    # Read the input
    lights = input()
    
    # Get the earliest time
    time = get_earliest_time(lights)
    
    # Print the output
    print(time)

if __name__ == '__main__':
    main()

