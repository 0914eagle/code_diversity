
def get_dog_attack(A, B, C, D, P, M, G):
    # Calculate the minute in the day during which the dogs are aggressive
    aggressive_minute_1 = (A + B) % 60
    aggressive_minute_2 = (C + D) % 60

    # Calculate the minute in the day during which the dogs are calm
    calm_minute_1 = (B + A) % 60
    calm_minute_2 = (D + C) % 60

    # Check which dog is aggressive during each minute
    if aggressive_minute_1 == P or aggressive_minute_2 == P:
        postman_attack = "one"
    else:
        postman_attack = "none"

    if aggressive_minute_1 == M or aggressive_minute_2 == M:
        milkman_attack = "one"
    else:
        milkman_attack = "none"

    if aggressive_minute_1 == G or aggressive_minute_2 == G:
        garbage_man_attack = "one"
    else:
        garbage_man_attack = "none"

    return postman_attack, milkman_attack, garbage_man_attack

