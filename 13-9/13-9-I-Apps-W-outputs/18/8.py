
def get_max_minutes(a_1, a_2):
    # Initialize variables
    minutes = 0
    charge_1 = a_1
    charge_2 = a_2
    
    # Game continues while both joysticks have a positive charge
    while charge_1 > 0 and charge_2 > 0:
        # Connect charger to a joystick only at the beginning of each minute
        if minutes % 2 == 0:
            charge_1 += 1
        else:
            charge_2 += 1
        
        # Joystick either discharges by 2 percent (if not connected to a charger) or charges by 1 percent (if connected to a charger)
        charge_1 = max(0, charge_1 - 2)
        charge_2 = max(0, charge_2 - 2)
        
        minutes += 1
    
    # Return the maximum number of minutes that the game can last
    return minutes

def main():
    a_1, a_2 = map(int, input().split())
    print(get_max_minutes(a_1, a_2))

if __name__ == '__main__':
    main()

