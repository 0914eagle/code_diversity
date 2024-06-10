
def get_attack_count(health, attack_damage):
    return (health - 1) // attack_damage + 1

def main():
    health, attack_damage = map(int, input().split())
    print(get_attack_count(health, attack_damage))

if __name__ == '__main__':
    main()

