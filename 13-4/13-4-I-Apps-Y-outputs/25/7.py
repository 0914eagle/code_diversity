
def get_dog_behavior(a, b, c, d):
    aggressive_period = a + c
    calm_period = b + d
    return aggressive_period, calm_period

def get_dog_attack(aggressive_period, calm_period, arrival_time):
    if arrival_time <= aggressive_period:
        return "both"
    elif arrival_time <= calm_period:
        return "one"
    else:
        return "none"

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    aggressive_period, calm_period = get_dog_behavior(a, b, c, d)
    print(get_dog_attack(aggressive_period, calm_period, p))
    print(get_dog_attack(aggressive_period, calm_period, m))
    print(get_dog_attack(aggressive_period, calm_period, g))

if __name__ == '__main__':
    main()

