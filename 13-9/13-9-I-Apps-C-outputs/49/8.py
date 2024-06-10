
def battle(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def):
    while yang_hp > 0 and monster_hp > 0:
        yang_hp -= max(0, monster_atk - yang_def)
        monster_hp -= max(0, yang_atk - monster_def)
    if yang_hp <= 0:
        return "Monster wins"
    else:
        return "Yang wins"

def buy_attributes(yang_hp, yang_atk, yang_def, hp_price, atk_price, def_price):
    total_bitcoins = 0
    while yang_hp < 100 and yang_atk < 100 and yang_def < 100:
        if yang_hp < 100 and hp_price <= total_bitcoins:
            yang_hp += 1
            total_bitcoins -= hp_price
        if yang_atk < 100 and atk_price <= total_bitcoins:
            yang_atk += 1
            total_bitcoins -= atk_price
        if yang_def < 100 and def_price <= total_bitcoins:
            yang_def += 1
            total_bitcoins -= def_price
    return total_bitcoins

def solve(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price):
    total_bitcoins = buy_attributes(yang_hp, yang_atk, yang_def, hp_price, atk_price, def_price)
    result = battle(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def)
    if result == "Yang wins":
        return total_bitcoins
    else:
        return -1

if __name__ == '__main__':
    yang_hp, yang_atk, yang_def = map(int, input().split())
    monster_hp, monster_atk, monster_def = map(int, input().split())
    hp_price, atk_price, def_price = map(int, input().split())
    print(solve(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, hp_price, atk_price, def_price))

