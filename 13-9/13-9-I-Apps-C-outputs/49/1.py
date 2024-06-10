
def get_minimum_bitcoins(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    # Initialize variables
    bitcoins_spent = 0
    hp_y_left = hp_y
    hp_m_left = hp_m

    # While the monster has HP left and Master Yang has HP left
    while hp_m_left > 0 and hp_y_left > 0:
        # Calculate damage dealt by Master Yang
        damage_dealt = max(0, atk_y - def_m)

        # Calculate damage taken by Master Yang
        damage_taken = max(0, atk_m - def_y)

        # Update HP of Master Yang and monster
        hp_y_left -= damage_taken
        hp_m_left -= damage_dealt

        # If Master Yang has more HP left than the monster, buy more HP
        if hp_y_left > hp_m_left:
            bitcoins_spent += (hp_y_left - hp_m_left) * h

    # If Master Yang has more HP left than the monster, he wins
    if hp_y_left > 0:
        return bitcoins_spent
    else:
        return -1

def get_minimum_bitcoins_optimized(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    # Initialize variables
    bitcoins_spent = 0
    hp_y_left = hp_y
    hp_m_left = hp_m

    # While the monster has HP left and Master Yang has HP left
    while hp_m_left > 0 and hp_y_left > 0:
        # Calculate damage dealt by Master Yang
        damage_dealt = max(0, atk_y - def_m)

        # Calculate damage taken by Master Yang
        damage_taken = max(0, atk_m - def_y)

        # Update HP of Master Yang and monster
        hp_y_left -= damage_taken
        hp_m_left -= damage_dealt

        # If Master Yang has more HP left than the monster, buy more HP
        if hp_y_left > hp_m_left:
            bitcoins_spent += (hp_y_left - hp_m_left) * h

    # If Master Yang has more HP left than the monster, he wins
    if hp_y_left > 0:
        return bitcoins_spent
    else:
        return -1

if __name__ == '__main__':
    hp_y, atk_y, def_y = map(int, input().split())
    hp_m, atk_m, def_m = map(int, input().split())
    h, a, d = map(int, input().split())
    print(get_minimum_bitcoins(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))
    print(get_minimum_bitcoins_optimized(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))

