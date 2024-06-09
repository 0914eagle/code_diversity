
def get_dogs_attack(arrival_times, aggressive_minutes):
    # Initialize variables
    postman_attack = False
    milkman_attack = False
    garbage_man_attack = False

    # Calculate the aggressive period for each dog
    aggressive_period_dog1 = aggressive_minutes[0]
    calm_period_dog1 = aggressive_minutes[1]
    aggressive_period_dog2 = aggressive_minutes[2]
    calm_period_dog2 = aggressive_minutes[3]

    # Determine which dog is aggressive at each minute
    for i in range(arrival_times[0], arrival_times[1] + 1):
        if i % (aggressive_period_dog1 + calm_period_dog1) < aggressive_period_dog1:
            postman_attack = True
        if i % (aggressive_period_dog2 + calm_period_dog2) < aggressive_period_dog2:
            milkman_attack = True
        if i % (aggressive_period_dog1 + calm_period_dog1) < aggressive_period_dog1 or i % (aggressive_period_dog2 + calm_period_dog2) < aggressive_period_dog2:
            garbage_man_attack = True

    # Determine which dogs attack each hero
    if postman_attack and milkman_attack and garbage_man_attack:
        postman_attack = "both"
        milkman_attack = "both"
        garbage_man_attack = "both"
    elif postman_attack and milkman_attack:
        postman_attack = "both"
        milkman_attack = "both"
        garbage_man_attack = "one"
    elif postman_attack and garbage_man_attack:
        postman_attack = "both"
        milkman_attack = "one"
        garbage_man_attack = "both"
    elif milkman_attack and garbage_man_attack:
        postman_attack = "one"
        milkman_attack = "both"
        garbage_man_attack = "both"
    elif postman_attack:
        postman_attack = "both"
        milkman_attack = "one"
        garbage_man_attack = "one"
    elif milkman_attack:
        postman_attack = "one"
        milkman_attack = "both"
        garbage_man_attack = "one"
    elif garbage_man_attack:
        postman_attack = "one"
        milkman_attack = "one"
        garbage_man_attack = "both"
    else:
        postman_attack = "none"
        milkman_attack = "none"
        garbage_man_attack = "none"

    return postman_attack, milkman_attack, garbage_man_attack

