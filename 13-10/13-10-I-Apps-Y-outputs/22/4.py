
def get_attacks_needed(health, attack_damage):
    attacks_needed = 0
    while health > 0:
        health -= attack_damage
        attacks_needed += 1
    return attacks_needed

def main():
    health, attack_damage = map(int, input().split())
    attacks_needed = get_attacks_needed(health, attack_damage)
    print(attacks_needed)

if __name__ == '__main__':
    main()

