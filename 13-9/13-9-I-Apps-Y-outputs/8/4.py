
def get_dog_attacks(A, B, C, D, P, M, G):
    # Calculate the number of minutes since midnight
    minutes_since_midnight = P + M + G

    # Calculate the number of minutes since the last calm period
    minutes_since_last_calm = minutes_since_midnight % (A + B)

    # Check if the first dog is aggressive
    if minutes_since_last_calm < A:
        dog_1_attack = True
    else:
        dog_1_attack = False

    # Check if the second dog is aggressive
    if minutes_since_last_calm < C:
        dog_2_attack = True
    else:
        dog_2_attack = False

    # Determine the number of dogs that attack each hero
    if dog_1_attack and dog_2_attack:
        dog_attacks = "both"
    elif dog_1_attack or dog_2_attack:
        dog_attacks = "one"
    else:
        dog_attacks = "none"

    return dog_attacks

