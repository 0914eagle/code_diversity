
def get_dog_behavior(a, b, c, d):
    aggressive_period = a
    calm_period = b
    aggressive_period2 = c
    calm_period2 = d
    return [aggressive_period, calm_period, aggressive_period2, calm_period2]

def get_dog_attack(postman_arrival, milkman_arrival, garbage_man_arrival, dog_behavior):
    aggressive_period = dog_behavior[0]
    calm_period = dog_behavior[1]
    aggressive_period2 = dog_behavior[2]
    calm_period2 = dog_behavior[3]
    dog_attack = []
    if postman_arrival % (aggressive_period + calm_period) < aggressive_period:
        dog_attack.append("postman")
    if milkman_arrival % (aggressive_period2 + calm_period2) < aggressive_period2:
        dog_attack.append("milkman")
    if garbage_man_arrival % (aggressive_period + calm_period) < aggressive_period:
        dog_attack.append("garbage man")
    if len(dog_attack) == 0:
        return "none"
    elif len(dog_attack) == 1:
        return dog_attack[0]
    else:
        return "both"

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    dog_behavior = get_dog_behavior(a, b, c, d)
    print(get_dog_attack(p, m, g, dog_behavior))

