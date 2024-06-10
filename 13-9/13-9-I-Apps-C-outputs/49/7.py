
def get_monster_hp(monster_hp, yang_atk, yang_def):
    return max(0, monster_hp - yang_atk + yang_def)

def get_yang_hp(yang_hp, monster_atk, monster_def):
    return max(0, yang_hp - monster_atk + monster_def)

def get_min_bitcoins(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price):
    # Initialize variables
    bitcoins_spent = 0
    yang_hp_remaining = yang_hp
    monster_hp_remaining = monster_hp

    # Loop until the monster's HP is <= 0 and Yang's HP is > 0
    while monster_hp_remaining > 0 and yang_hp_remaining > 0:
        # Update the monster's HP
        monster_hp_remaining = get_monster_hp(monster_hp_remaining, yang_atk, yang_def)

        # Update Yang's HP
        yang_hp_remaining = get_yang_hp(yang_hp_remaining, monster_atk, monster_def)

        # Check if Yang has enough HP to attack the monster
        if yang_hp_remaining > 0:
            # Calculate the number of bitcoins needed to buy HP
            hp_needed = max(1, yang_hp_remaining - yang_hp + 1)
            bitcoins_spent += hp_needed * hp_price

            # Update Yang's HP
            yang_hp_remaining += hp_needed

        # Check if Yang has enough ATK to attack the monster
        if yang_atk < monster_def:
            # Calculate the number of bitcoins needed to buy ATK
            atk_needed = max(1, monster_def - yang_atk + 1)
            bitcoins_spent += atk_needed * atk_price

            # Update Yang's ATK
            yang_atk += atk_needed

        # Check if Yang has enough DEF to defend against the monster
        if yang_def < monster_atk:
            # Calculate the number of bitcoins needed to buy DEF
            def_needed = max(1, monster_atk - yang_def + 1)
            bitcoins_spent += def_needed * def_price

            # Update Yang's DEF
            yang_def += def_needed

    # Return the minimum number of bitcoins needed to win
    return bitcoins_spent

def main():
    # Read input
    yang_hp, yang_atk, yang_def = map(int, input().split())
    monster_hp, monster_atk, monster_def = map(int, input().split())
    hp_price, atk_price, def_price = map(int, input().split())

    # Calculate the minimum number of bitcoins needed to win
    bitcoins_needed = get_min_bitcoins(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price)

    # Print output
    print(bitcoins_needed)

if __name__ == '__main__':
    main()

