
def solve(A, B, C, D, P, M, G):
    # Calculate the number of aggressive minutes for each dog
    aggressive_minutes_dog1 = A + B
    aggressive_minutes_dog2 = C + D

    # Calculate the total number of aggressive minutes
    total_aggressive_minutes = aggressive_minutes_dog1 + aggressive_minutes_dog2

    # Calculate the number of calm minutes for each dog
    calm_minutes_dog1 = 60 - A
    calm_minutes_dog2 = 60 - C

    # Calculate the total number of calm minutes
    total_calm_minutes = calm_minutes_dog1 + calm_minutes_dog2

    # Calculate the number of aggressive minutes before the arrival time of the postman
    aggressive_minutes_before_postman = P % total_aggressive_minutes

    # Calculate the number of calm minutes before the arrival time of the postman
    calm_minutes_before_postman = (P - aggressive_minutes_before_postman) % total_calm_minutes

    # Calculate the number of aggressive minutes before the arrival time of the milkman
    aggressive_minutes_before_milkman = M % total_aggressive_minutes

    # Calculate the number of calm minutes before the arrival time of the milkman
    calm_minutes_before_milkman = (M - aggressive_minutes_before_milkman) % total_calm_minutes

    # Calculate the number of aggressive minutes before the arrival time of the garbage man
    aggressive_minutes_before_garbage_man = G % total_aggressive_minutes

    # Calculate the number of calm minutes before the arrival time of the garbage man
    calm_minutes_before_garbage_man = (G - aggressive_minutes_before_garbage_man) % total_calm_minutes

    # Determine which dogs attack which heros
    if aggressive_minutes_before_postman > calm_minutes_before_postman:
        postman_attacked_by = "one"
    elif aggressive_minutes_before_postman < calm_minutes_before_postman:
        postman_attacked_by = "none"
    else:
        postman_attacked_by = "both"

    if aggressive_minutes_before_milkman > calm_minutes_before_milkman:
        milkman_attacked_by = "one"
    elif aggressive_minutes_before_milkman < calm_minutes_before_milkman:
        milkman_attacked_by = "none"
    else:
        milkman_attacked_by = "both"

    if aggressive_minutes_before_garbage_man > calm_minutes_before_garbage_man:
        garbage_man_attacked_by = "one"
    elif aggressive_minutes_before_garbage_man < calm_minutes_before_garbage_man:
        garbage_man_attacked_by = "none"
    else:
        garbage_man_attacked_by = "both"

    return postman_attacked_by, milkman_attacked_by, garbage_man_attacked_by

