
def get_aggressive_dog(minute, aggressive_minutes, calm_minutes):
    
    aggressive_dog = 1 if minute % (aggressive_minutes + calm_minutes) < aggressive_minutes else 2
    return aggressive_dog

def get_attacking_dogs(postman_minute, milkman_minute, garbage_man_minute, aggressive_minutes, calm_minutes):
    
    postman_dog = get_aggressive_dog(postman_minute, aggressive_minutes, calm_minutes)
    milkman_dog = get_aggressive_dog(milkman_minute, aggressive_minutes, calm_minutes)
    garbage_man_dog = get_aggressive_dog(garbage_man_minute, aggressive_minutes, calm_minutes)
    attacking_dogs = [postman_dog, milkman_dog, garbage_man_dog]
    return attacking_dogs

def main():
    aggressive_minutes, calm_minutes, postman_minute, milkman_minute, garbage_man_minute = map(int, input().split())
    attacking_dogs = get_attacking_dogs(postman_minute, milkman_minute, garbage_man_minute, aggressive_minutes, calm_minutes)
    print(attacking_dogs)

if __name__ == '__main__':
    main()

