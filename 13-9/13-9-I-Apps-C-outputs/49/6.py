
def get_monster_hp(monster_hp, monster_atk, monster_def, yang_atk):
    return max(0, monster_hp - max(0, yang_atk - monster_def))

def get_yang_hp(yang_hp, yang_atk, yang_def, monster_atk):
    return max(0, yang_hp - max(0, monster_atk - yang_def))

def get_min_bitcoins(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price):
    bitcoins_spent = 0
    while yang_hp > 0 and monster_hp > 0:
        monster_hp = get_monster_hp(monster_hp, monster_atk, monster_def, yang_atk)
        yang_hp = get_yang_hp(yang_hp, yang_atk, yang_def, monster_atk)
        bitcoins_spent += hp_price
        if yang_hp == 0:
            break
        bitcoins_spent += atk_price
        if monster_hp == 0:
            break
        bitcoins_spent += def_price
    return bitcoins_spent

def main():
    yang_hp, yang_atk, yang_def = map(int, input().split())
    monster_hp, monster_atk, monster_def = map(int, input().split())
    hp_price, atk_price, def_price = map(int, input().split())
    print(get_min_bitcoins(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price))

if __name__ == '__main__':
    main()

