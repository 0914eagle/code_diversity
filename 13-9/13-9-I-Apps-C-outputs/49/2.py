
def get_min_bitcoins(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    # Initialize variables
    bitcoins_spent = 0
    hp_y_left = hp_y
    atk_y_left = atk_y
    def_y_left = def_y
    hp_m_left = hp_m
    atk_m_left = atk_m
    def_m_left = def_m

    # Buy HP, ATK, and DEF until Master Yang's HP is greater than or equal to the monster's HP
    while hp_y_left < hp_m_left:
        hp_y_left += h
        atk_y_left += a
        def_y_left += d
        bitcoins_spent += h + a + d

    # Calculate the number of times the battle will take place
    num_battles = (hp_y_left + hp_m_left) // 2

    # Simulate the battle
    for _ in range(num_battles):
        # Calculate damage dealt by Master Yang
        damage_dealt = max(0, atk_y_left - def_m_left)

        # Calculate damage dealt by the monster
        damage_taken = max(0, atk_m_left - def_y_left)

        # Apply damage to both characters
        hp_y_left -= damage_taken
        hp_m_left -= damage_dealt

    # Return the minimum number of bitcoins spent
    return bitcoins_spent

def main():
    hp_y, atk_y, def_y = map(int, input().split())
    hp_m, atk_m, def_m = map(int, input().split())
    h, a, d = map(int, input().split())
    print(get_min_bitcoins(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))

if __name__ == '__main__':
    main()

