
def get_max_fruits(a, b, c):
    if a + b + c == 0:
        return 0

    lemons = a
    apples = b
    pears = c

    while lemons > 0 and apples > 0 and pears > 0:
        if lemons % 2 == 0 and apples % 4 == 0 and pears % 4 == 0:
            break

        if lemons % 2 == 1:
            lemons -= 1
        if apples % 4 == 1:
            apples -= 1
        if pears % 4 == 1:
            pears -= 1

    return lemons + apples + pears

