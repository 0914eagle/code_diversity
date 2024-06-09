
t = int(input())

for _ in range(t):
    n = int(input())
    pin_codes = []
    for _ in range(n):
        pin_codes.append(input())

    changes = 0
    new_pin_codes = []
    seen = set()

    for pin in pin_codes:
        if pin in seen:
            changes += 1
            for i in range(4):
                new_digit = (int(pin[i]) + 1) % 10
                new_pin = pin[:i] + str(new_digit) + pin[i+1:]
                if new_pin not in seen:
                    seen.add(new_pin)
                    new_pin_codes.append(new_pin)
                    break
        else:
            seen.add(pin)
            new_pin_codes.append(pin)

    print(changes)
    for new_pin in new_pin_codes:
        print(new_pin)
