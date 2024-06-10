
def determine_dog_attacks(a, b, c, d, p, m, g):
    # Initialize variables
    aggressive_dog_1 = True
    aggressive_dog_2 = True
    dog_1_calm_time = b
    dog_2_calm_time = d
    postman_attacked = False
    milkman_attacked = False
    garbage_man_attacked = False

    # Determine which dogs are aggressive during each minute of the day
    for i in range(1, 999):
        if i == p:
            postman_attacked = aggressive_dog_1 or aggressive_dog_2
        if i == m:
            milkman_attacked = aggressive_dog_1 or aggressive_dog_2
        if i == g:
            garbage_man_attacked = aggressive_dog_1 or aggressive_dog_2

        # Update the aggressive status of the dogs
        if aggressive_dog_1:
            dog_1_calm_time -= 1
            if dog_1_calm_time == 0:
                aggressive_dog_1 = False
                dog_1_calm_time = b
        if aggressive_dog_2:
            dog_2_calm_time -= 1
            if dog_2_calm_time == 0:
                aggressive_dog_2 = False
                dog_2_calm_time = d

    # Determine which dogs attacked each of the three individuals
    if postman_attacked and milkman_attacked and garbage_man_attacked:
        return "both"
    elif postman_attacked or milkman_attacked or garbage_man_attacked:
        return "one"
    else:
        return "none"

def main():
    a, b, c, d, p, m, g = map(int, input().split())
    print(determine_dog_attacks(a, b, c, d, p, m, g))

if __name__ == '__main__':
    main()

