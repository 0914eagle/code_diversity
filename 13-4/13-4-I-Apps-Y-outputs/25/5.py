
def get_dog_behavior(a, b, c, d):
    aggressive_duration = a + c
    calm_duration = b + d
    total_duration = aggressive_duration + calm_duration
    return aggressive_duration, calm_duration, total_duration

def get_dog_attack(aggressive_duration, calm_duration, arrival_time):
    if arrival_time <= aggressive_duration:
        return "both"
    elif arrival_time <= calm_duration:
        return "one"
    else:
        return "none"

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    aggressive_duration, calm_duration, total_duration = get_dog_behavior(a, b, c, d)
    postman_attack = get_dog_attack(aggressive_duration, calm_duration, p)
    milkman_attack = get_dog_attack(aggressive_duration, calm_duration, m)
    garbage_man_attack = get_dog_attack(aggressive_duration, calm_duration, g)
    print(postman_attack)
    print(milkman_attack)
    print(garbage_man_attack)

if __name__ == '__main__':
    main()

