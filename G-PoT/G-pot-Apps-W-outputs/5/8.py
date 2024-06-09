
t = int(input())

for _ in range(t):
    n = int(input())
    pins = []
    for _ in range(n):
        pins.append(input())

    changes = 0
    changed_pins = []
    seen_pins = set()

    for pin in pins:
        if pin in seen_pins:
            changes += 1
            for i in range(4):
                new_pin = pin[:i] + str((int(pin[i]) + 1) % 10) + pin[i+1:]
                if new_pin not in seen_pins:
                    changed_pins.append(new_pin)
                    seen_pins.add(new_pin)
                    break
        else:
            changed_pins.append(pin)
            seen_pins.add(pin)

    print(changes)
    for changed_pin in changed_pins:
        print(changed_pin)
