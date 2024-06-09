
def get_dog_behavior(a, b, c, d):
    aggressive_dog = 1
    calm_dog = 2
    current_dog = aggressive_dog
    current_time = 0
    dog_behavior = []
    while current_time < 1440:
        if current_dog == aggressive_dog:
            dog_behavior.append(current_dog)
            current_dog = calm_dog
        else:
            dog_behavior.append(current_dog)
            current_dog = aggressive_dog
        current_time += 1
    return dog_behavior

def get_dog_attack(dog_behavior, p, m, g):
    dog_attack = []
    for i in range(len(dog_behavior)):
        if dog_behavior[i] == 1 and (i + 1) % (p + m + g) in [1, p, p + m]:
            dog_attack.append('both')
        elif dog_behavior[i] == 1 and (i + 1) % (p + m + g) in [p + 1, p + m]:
            dog_attack.append('one')
        else:
            dog_attack.append('none')
    return dog_attack

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    dog_behavior = get_dog_behavior(a, b, c, d)
    dog_attack = get_dog_attack(dog_behavior, p, m, g)
    print('both')
    print('one')
    print('none')

if __name__ == '__main__':
    main()

