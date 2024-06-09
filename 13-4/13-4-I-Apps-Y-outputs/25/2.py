
def get_dog_behavior(a, b, c, d):
    # Returns a tuple of dog behavior, where the first element is the aggressive period and the second element is the calm period
    return (a, b), (c, d)

def get_dog_attack(postman_time, milkman_time, garbage_man_time, dog_behavior):
    # Returns a tuple of dog attack, where the first element is the postman attack, the second element is the milkman attack, and the third element is the garbage man attack
    postman_attack = False
    milkman_attack = False
    garbage_man_attack = False

    for i in range(len(dog_behavior)):
        aggressive_period, calm_period = dog_behavior[i]
        if postman_time in range(aggressive_period, calm_period):
            postman_attack = True
        if milkman_time in range(aggressive_period, calm_period):
            milkman_attack = True
        if garbage_man_time in range(aggressive_period, calm_period):
            garbage_man_attack = True

    return postman_attack, milkman_attack, garbage_man_attack

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    dog_behavior = get_dog_behavior(a, b, c, d)
    postman_attack, milkman_attack, garbage_man_attack = get_dog_attack(p, m, g, dog_behavior)

    if postman_attack and milkman_attack and garbage_man_attack:
        print("both")
    elif postman_attack or milkman_attack or garbage_man_attack:
        print("one")
    else:
        print("none")

if __name__ == '__main__':
    main()

