
def get_bitcoins_needed(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, h, a, d):
    # Calculate the minimum bitcoins needed to buy the required attributes
    bitcoins_needed = h * (yang_hp - monster_hp) + a * (yang_atk - monster_atk) + d * (yang_def - monster_def)
    return bitcoins_needed

def main():
    yang_hp, yang_atk, yang_def = map(int, input().split())
    monster_hp, monster_atk, monster_def = map(int, input().split())
    h, a, d = map(int, input().split())
    bitcoins_needed = get_bitcoins_needed(yang_hp, yang_atk, yang_def, monster_hp, monster_atk, monster_def, h, a, d)
    print(bitcoins_needed)

if __name__ == '__main__':
    main()

