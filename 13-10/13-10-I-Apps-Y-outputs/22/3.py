
def get_attack_count(monster_health, attack_power):
    return (monster_health - 1) // attack_power + 1

def main():
    monster_health, attack_power = map(int, input().split())
    print(get_attack_count(monster_health, attack_power))

if __name__ == '__main__':
    main()

