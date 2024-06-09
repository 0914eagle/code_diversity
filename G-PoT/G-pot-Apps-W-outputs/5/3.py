
t = int(input())

for _ in range(t):
    n = int(input())
    pin_codes = []
    for _ in range(n):
        pin_codes.append(input())

    changes = 0
    changed_pins = []
    for i in range(n):
        if pin_codes.count(pin_codes[i]) > 1:
            changes += 1
            for j in range(10):
                new_pin = pin_codes[i][:3] + str(j)
                if new_pin not in changed_pins:
                    changed_pins.append(new_pin)
                    pin_codes[i] = new_pin
                    break

    print(changes)
    for pin in pin_codes:
        print(pin)