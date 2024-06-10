
def get_dog_attack(aggressive_time, calm_time, current_time):
    if current_time % (aggressive_time + calm_time) < aggressive_time:
        return 1
    else:
        return 0

def postman_dog_attack(postman_time, aggressive_time, calm_time):
    return get_dog_attack(aggressive_time, calm_time, postman_time)

def milkman_dog_attack(milkman_time, aggressive_time, calm_time):
    return get_dog_attack(aggressive_time, calm_time, milkman_time)

def garbage_man_dog_attack(garbage_man_time, aggressive_time, calm_time):
    return get_dog_attack(aggressive_time, calm_time, garbage_man_time)

if __name__ == '__main__':
    aggressive_time, calm_time, postman_time, milkman_time, garbage_man_time = map(int, input().split())
    print(postman_dog_attack(postman_time, aggressive_time, calm_time))
    print(milkman_dog_attack(milkman_time, aggressive_time, calm_time))
    print(garbage_man_dog_attack(garbage_man_time, aggressive_time, calm_time))

