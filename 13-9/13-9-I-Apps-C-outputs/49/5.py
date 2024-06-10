
def get_min_bitcoins(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
    # Initialize variables
    bitcoins_spent = 0
    hp_diff = hp_y - hp_m
    atk_diff = atk_y - atk_m
    def_diff = def_y - def_m
    
    # Buy HP
    while hp_diff > 0:
        bitcoins_spent += h
        hp_diff -= h
    
    # Buy ATK
    while atk_diff > 0:
        bitcoins_spent += a
        atk_diff -= a
    
    # Buy DEF
    while def_diff > 0:
        bitcoins_spent += d
        def_diff -= d
    
    return bitcoins_spent

def main():
    hp_y, atk_y, def_y = map(int, input().split())
    hp_m, atk_m, def_m = map(int, input().split())
    h, a, d = map(int, input().split())
    print(get_min_bitcoins(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d))

if __name__ == '__main__':
    main()

