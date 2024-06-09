
def get_dog_behavior(a, b, c, d):
    aggressive_periods = [(a, False), (b, True), (c, False), (d, True)]
    aggressive_periods.sort()
    return aggressive_periods

def get_dog_attack(aggressive_periods, arrival_time):
    if arrival_time < aggressive_periods[0][0]:
        return "none"
    if arrival_time == aggressive_periods[0][0]:
        return "one" if aggressive_periods[0][1] else "none"
    if arrival_time == aggressive_periods[1][0]:
        return "both"
    if arrival_time > aggressive_periods[1][0]:
        return "one"

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    aggressive_periods = get_dog_behavior(a, b, c, d)
    print(get_dog_attack(aggressive_periods, p))
    print(get_dog_attack(aggressive_periods, m))
    print(get_dog_attack(aggressive_periods, g))

if __name__ == '__main__':
    main()

