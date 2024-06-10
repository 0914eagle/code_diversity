
def get_max_minutes(a1, a2):
    minutes = 0
    while a1 > 0 and a2 > 0:
        if a1 == 100:
            a1 = 200
        if a2 == 100:
            a2 = 200
        a1 -= 2
        a2 -= 2
        minutes += 1
    return minutes

def get_max_minutes_with_charger(a1, a2):
    minutes = 0
    while a1 > 0 and a2 > 0:
        if a1 == 100:
            a1 = 200
        if a2 == 100:
            a2 = 200
        a1 -= 2
        a2 -= 2
        minutes += 1
        if a1 == 0:
            a1 = 100
        if a2 == 0:
            a2 = 100
    return minutes

if __name__ == '__main__':
    a1, a2 = map(int, input().split())
    print(get_max_minutes(a1, a2))
    print(get_max_minutes_with_charger(a1, a2))

