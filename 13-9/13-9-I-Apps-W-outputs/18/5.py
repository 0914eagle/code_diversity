
def charge_joystick(joystick_charge, charger_power):
    if joystick_charge + charger_power > 100:
        return 100
    else:
        return joystick_charge + charger_power

def discharge_joystick(joystick_charge):
    return max(joystick_charge - 2, 0)

def find_max_minutes(joystick1_charge, joystick2_charge):
    minutes = 0
    while joystick1_charge > 0 and joystick2_charge > 0:
        minutes += 1
        joystick1_charge = charge_joystick(joystick1_charge, 1)
        joystick2_charge = charge_joystick(joystick2_charge, 1)
        joystick1_charge = discharge_joystick(joystick1_charge)
        joystick2_charge = discharge_joystick(joystick2_charge)
    return minutes

def main():
    joystick1_charge, joystick2_charge = map(int, input().split())
    print(find_max_minutes(joystick1_charge, joystick2_charge))

if __name__ == '__main__':
    main()

