
t = int(input())

for _ in range(t):
    n = int(input())
    pin_codes = []
    for _ in range(n):
        pin_codes.append(input())

    changes = 0
    changed_pins = []
    seen_pins = set()

    for pin in pin_codes:
        if pin in seen_pins:
            changes += 1
            for i in range(4):
                new_pin = list(pin)
                for j in range(10):
                    if str(j) != new_pin[i]:
                        new_pin[i] = str(j)
                        new_pin_str = ''.join(new_pin)
                        if new_pin_str not in seen_pins:
                            seen_pins.add(new_pin_str)
                            changed_pins.append(new_pin_str)
                            break
        else:
            seen_pins.add(pin)
            changed_pins.append(pin)

    print(changes)
    for changed_pin in changed_pins:
        print(changed_pin)
