
def get_max_minutes(a_1, a_2):
    # Initialize variables
    minutes = 0
    charge_1 = a_1
    charge_2 = a_2
    
    # While both joysticks have positive charge
    while charge_1 > 0 and charge_2 > 0:
        # Connect charger to the joystick with lower charge
        if charge_1 < charge_2:
            charge_1 += 1
        else:
            charge_2 += 1
        
        # Discharge both joysticks
        charge_1 -= 2
        charge_2 -= 2
        
        # Increment minutes
        minutes += 1
    
    # Return maximum number of minutes
    return minutes

def main():
    a_1, a_2 = map(int, input().split())
    print(get_max_minutes(a_1, a_2))

if __name__ == '__main__':
    main()

