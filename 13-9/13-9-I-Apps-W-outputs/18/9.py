
def get_max_minutes(a1, a2):
    # Initialize variables
    minutes = 0
    charged_a1 = a1
    charged_a2 = a2
    
    # Loop until both joysticks are discharged
    while charged_a1 > 0 and charged_a2 > 0:
        # Increment minutes
        minutes += 1
        
        # Charged joystick
        if charged_a1 < a1:
            charged_a1 += 1
        if charged_a2 < a2:
            charged_a2 += 1
        
        # Discharged joystick
        if charged_a1 == 0:
            charged_a1 = a1
        if charged_a2 == 0:
            charged_a2 = a2
    
    # Return maximum minutes
    return minutes

def main():
    a1, a2 = map(int, input().split())
    print(get_max_minutes(a1, a2))

if __name__ == '__main__':
    main()

