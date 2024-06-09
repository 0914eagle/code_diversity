
def get_attacking_dogs(A, B, C, D, P, M, G):
    # Calculate the minute in the day when the first dog will be aggressive
    first_aggressive_minute = (P + A) % (A + B)
    
    # Calculate the minute in the day when the second dog will be aggressive
    second_aggressive_minute = (M + C) % (C + D)
    
    # Check if the postman is attacked by either dog
    if first_aggressive_minute == P or second_aggressive_minute == P:
        postman_attacked = "one"
    else:
        postman_attacked = "none"
    
    # Check if the milkman is attacked by either dog
    if first_aggressive_minute == M or second_aggressive_minute == M:
        milkman_attacked = "one"
    else:
        milkman_attacked = "none"
    
    # Check if the garbage man is attacked by either dog
    if first_aggressive_minute == G or second_aggressive_minute == G:
        garbage_man_attacked = "one"
    else:
        garbage_man_attacked = "none"
    
    return postman_attacked, milkman_attacked, garbage_man_attacked

