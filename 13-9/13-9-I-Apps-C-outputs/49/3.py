
def get_min_bitcoins_to_win(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, h, a, d):
    # Initialize variables
    bitcoins_spent = 0
    yang_hp_left = yang_hp
    monster_hp_left = monster_hp

    # Buy attributes until one of the players dies
    while yang_hp_left > 0 and monster_hp_left > 0:
        # Buy HP
        hp_bought = min(yang_hp_left, h)
        bitcoins_spent += hp_bought * h
        yang_hp_left -= hp_bought

        # Buy ATK
        atk_bought = min(yang_hp_left, a)
        bitcoins_spent += atk_bought * a
        yang_atk += atk_bought

        # Buy DEF
        def_bought = min(yang_hp_left, d)
        bitcoins_spent += def_bought * d
        yang_def += def_bought

        # Update HP and ATK of the monster
        monster_hp_left = max(0, monster_hp_left - (yang_atk - monster_def))
        monster_atk += 1

    # Return the minimum number of bitcoins spent to win
    if yang_hp_left > 0:
        return bitcoins_spent
    else:
        return -1

def main():
    yang_hp, yang_atk, yang_def = map(int, input().split())
    monster_hp, monster_atk, monster_def = map(int, input().split())
    h, a, d = map(int, input().split())
    print(get_min_bitcoins_to_win(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, h, a, d))

if __name__ == '__main__':
    main()

