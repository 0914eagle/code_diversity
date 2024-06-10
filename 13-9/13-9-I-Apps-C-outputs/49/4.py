
def get_min_bitcoins_to_win(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    # Initialize variables
    bitcoins_spent = 0
    hp_y_left = hp_y
    atk_y_left = atk_y
    def_y_left = def_y
    hp_m_left = hp_m
    atk_m_left = atk_m
    def_m_left = def_m

    # Buy attributes until Monster's HP is 0 and Master Yang's HP is greater than 0
    while hp_m_left > 0 and hp_y_left > 0:
        # Calculate damage dealt by Monster and Master Yang
        damage_dealt_by_monster = max(0, atk_y_left - def_m_left)
        damage_dealt_by_master_yang = max(0, atk_m_left - def_y_left)

        # Update HP and attributes
        hp_y_left -= damage_dealt_by_monster
        hp_m_left -= damage_dealt_by_master_yang
        atk_y_left += h
        atk_m_left += a
        def_y_left += d
        def_m_left += d

        # Increase bitcoins spent
        bitcoins_spent += h + a + d

    # Return minimum bitcoins needed to win
    if hp_y_left > 0:
        return -1
    else:
        return bitcoins_spent

def main():
    hp_y, atk_y, def_y = map(int, input().split())
    hp_m, atk_m, def_m = map(int, input().split())
    h, a, d = map(int, input().split())
    print(get_min_bitcoins_to_win(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))

if __name__ == '__main__':
    main()

