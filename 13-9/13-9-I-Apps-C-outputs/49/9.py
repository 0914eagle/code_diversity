
def buy_hp(hp, hp_price):
    return hp * hp_price

def buy_atk(atk, atk_price):
    return atk * atk_price

def buy_def(def, def_price):
    return def * def_price

def calculate_bitcoins_needed(hp_y, atk_y, def_y, hp_m, atk_m, def_m, hp_price, atk_price, def_price):
    bitcoins_needed = 0
    while hp_y > 0 and hp_m > 0:
        bitcoins_needed += buy_hp(hp_y, hp_price)
        bitcoins_needed += buy_atk(atk_y, atk_price)
        bitcoins_needed += buy_def(def_y, def_price)
        hp_y = max(0, hp_y - max(0, atk_m - def_y))
        hp_m = max(0, hp_m - max(0, atk_y - def_m))
    return bitcoins_needed

def main():
    hp_y, atk_y, def_y = map(int, input().split())
    hp_m, atk_m, def_m = map(int, input().split())
    hp_price, atk_price, def_price = map(int, input().split())
    print(calculate_bitcoins_needed(hp_y, atk_y, def_y, hp_m, atk_m, def_m, hp_price, atk_price, def_price))

if __name__ == '__main__':
    main()

