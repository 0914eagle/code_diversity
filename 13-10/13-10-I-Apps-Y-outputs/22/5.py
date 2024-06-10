
def get_attack_count(monster_health, attack_damage):
    return (monster_health - 1) // attack_damage + 1

def main():
    monster_health, attack_damage = map(int, input().split())
    print(get_attack_count(monster_health, attack_damage))

if __name__ == '__main__':
    main()

